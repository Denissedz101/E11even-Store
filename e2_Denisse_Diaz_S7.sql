-- 1) Se requiere generar un proceso automático que permita mantener actualizada la tabla RESUMEN_COSTOS (costos y cantidad de atenciones por período de tiempo) considerando los cambios sobre la tabla ATENCIÓN

CREATE OR REPLACE TRIGGER tr_actualiza_resumen_costos_atenciones
AFTER INSERT OR UPDATE OR DELETE ON ATENCION
FOR EACH ROW
DECLARE
    v_periodo_ant   VARCHAR2(7);
    v_periodo_nuevo VARCHAR2(7);
BEGIN
    IF INSERTING THEN
        v_periodo_nuevo := TO_CHAR(:NEW.fecha_atencion, 'MM-YYYY');

        -- Verificamos si el periodo existe
        IF EXISTS (SELECT 1 FROM RESUMEN_COSTOS WHERE periodo = v_periodo_nuevo) THEN
            UPDATE RESUMEN_COSTOS
            SET total_atenciones = total_atenciones + 1,
                costo_total = costo_total + :NEW.costo
            WHERE periodo = v_periodo_nuevo;
        ELSE
            INSERT INTO RESUMEN_COSTOS (periodo, total_atenciones, costo_total)
            VALUES (v_periodo_nuevo, 1, :NEW.costo);
        END IF;

    ELSIF DELETING THEN
        v_periodo_ant := TO_CHAR(:OLD.fecha_atencion, 'MM-YYYY');

        UPDATE RESUMEN_COSTOS
        SET total_atenciones = total_atenciones - 1,
            costo_total = costo_total - :OLD.costo
        WHERE periodo = v_periodo_ant;

        -- Eliminamos si ya no hay atenciones
        DELETE FROM RESUMEN_COSTOS
        WHERE periodo = v_periodo_ant AND total_atenciones = 0;

    ELSIF UPDATING THEN
        v_periodo_ant := TO_CHAR(:OLD.fecha_atencion, 'MM-YYYY');
        v_periodo_nuevo := TO_CHAR(:NEW.fecha_atencion, 'MM-YYYY');

        IF v_periodo_ant = v_periodo_nuevo THEN
            -- Mismo periodo, solo cambia el costo
            UPDATE RESUMEN_COSTOS
            SET costo_total = costo_total - :OLD.costo + :NEW.costo
            WHERE periodo = v_periodo_nuevo;
        ELSE
            -- Eliminamos el costo de periodo antiguo
            UPDATE RESUMEN_COSTOS
            SET total_atenciones = total_atenciones - 1,
                costo_total = costo_total - :OLD.costo
            WHERE periodo = v_periodo_ant;

            DELETE FROM RESUMEN_COSTOS
            WHERE periodo = v_periodo_ant AND total_atenciones = 0;

            -- Agregamos el costo al nuevo periodo
            IF EXISTS (SELECT 1 FROM RESUMEN_COSTOS WHERE periodo = v_periodo_nuevo) THEN
                UPDATE RESUMEN_COSTOS
                SET total_atenciones = total_atenciones + 1,
                    costo_total = costo_total + :NEW.costo
                WHERE periodo = v_periodo_nuevo;
            ELSE
                INSERT INTO RESUMEN_COSTOS (periodo, total_atenciones, costo_total)
                VALUES (v_periodo_nuevo, 1, :NEW.costo);
            END IF;
        END IF;
    END IF;
END tr_actualiza_resumen_costos_atenciones;
/

-- probar proceso creado --

-- 1. Modificar el costo de la atención con ID = 476 a $28.000

UPDATE ATENCION
SET costo = 28000
WHERE ate_id = 476;

-- 2. Insertar una nueva atención con ID = 573 (fecha 23-03-2022)

INSERT INTO ATENCION (ate_id, fecha_atencion, hr_atencion, costo, med_run, pac_run)
VALUES (573, TO_DATE('23-03-2022', 'DD-MM-YYYY'), '13:45', 29000, 9827836, 7378093);

-- 3. Insertar una nueva atención con ID = 574 (fecha 23-09-2022)

INSERT INTO ATENCION (ate_id, fecha_atencion, hr_atencion, costo, med_run, pac_run)
VALUES (574, TO_DATE('23-09-2022', 'DD-MM-YYYY'), '13:45', 15000, 9827836, 7378093);

-- Revisamos la tabla
SELECT * FROM RESUMEN_COSTOS ORDER BY periodo;

-- 2) Por políticas definidas en la organización cada año se aplican recargos a los pacientes cuyo sistema de salud sea de las FUERZAS ARMADA la cual está registrada año a año en la tabla RECARGO_ATENCION_FFAA.

CREATE OR REPLACE TRIGGER tr_actualiza_recargo_atencion_ffaa
AFTER INSERT OR UPDATE ON PACIENTE
FOR EACH ROW
DECLARE
    v_tipo_salud_ant SALUD.tipo_sal_id%TYPE;
    v_tipo_salud_nuevo SALUD.tipo_sal_id%TYPE;
    v_anno_max NUMBER;
    v_porc_actual NUMBER(3,2);
    v_anno_actual NUMBER := EXTRACT(YEAR FROM SYSDATE);
    v_existe NUMBER;
BEGIN
    -- Obtenemos el tipo de salud del nuevo valor
    SELECT tipo_sal_id INTO v_tipo_salud_nuevo
    FROM SALUD
    WHERE sal_id = :NEW.sal_id;

    IF INSERTING THEN
        IF v_tipo_salud_nuevo = 'FA' THEN
            -- Obtenemos el ultimo porcentaje registrado
            SELECT MAX(anno_recargo) INTO v_anno_max FROM RECARGO_ATENCION_FFAA;
            SELECT porc_recargo INTO v_porc_actual
            FROM RECARGO_ATENCION_FFAA
            WHERE anno_recargo = v_anno_max;

            -- Verificamos si el año actual ya existe
            SELECT COUNT(*) INTO v_existe
            FROM RECARGO_ATENCION_FFAA
            WHERE anno_recargo = v_anno_actual;

            IF v_existe = 0 THEN
                INSERT INTO RECARGO_ATENCION_FFAA (anno_recargo, porc_recargo)
                VALUES (v_anno_actual, v_porc_actual + 0.01);
            ELSE
                UPDATE RECARGO_ATENCION_FFAA
                SET porc_recargo = v_porc_actual + 0.01
                WHERE anno_recargo = v_anno_actual;
            END IF;
        END IF;

    ELSIF UPDATING THEN
        IF :OLD.sal_id != :NEW.sal_id THEN
            -- Tipo de salud antiguo
            SELECT tipo_sal_id INTO v_tipo_salud_ant
            FROM SALUD
            WHERE sal_id = :OLD.sal_id;

            IF v_tipo_salud_ant != 'FA' AND v_tipo_salud_nuevo = 'FA' THEN
                -- Obtenemos el ultimo porcentaje registrado
                SELECT MAX(anno_recargo) INTO v_anno_max FROM RECARGO_ATENCION_FFAA;
                SELECT porc_recargo INTO v_porc_actual
                FROM RECARGO_ATENCION_FFAA
                WHERE anno_recargo = v_anno_max;

                -- Verificamos si el año actual ya existe
                SELECT COUNT(*) INTO v_existe
                FROM RECARGO_ATENCION_FFAA
                WHERE anno_recargo = v_anno_actual;

                IF v_existe = 0 THEN
                    INSERT INTO RECARGO_ATENCION_FFAA (anno_recargo, porc_recargo)
                    VALUES (v_anno_actual, v_porc_actual + 0.01);
                ELSE
                    UPDATE RECARGO_ATENCION_FFAA
                    SET porc_recargo = v_porc_actual + 0.01
                    WHERE anno_recargo = v_anno_actual;
                END IF;
            END IF;
        END IF;
    END IF;
END tr_actualiza_recargo_atencion_ffaa;
/

-- Probar proceso automatizado --

-- 1. Modificamos el costo de la atención con ID = 476
UPDATE ATENCION
SET costo = 28000
WHERE ate_id = 476;

-- 2. Insertamos paciente afiliado a FFAA
INSERT INTO PACIENTE (pac_run, dv_run, pnombre, snombre, apaterno, amaterno,fecha_nacimiento, telefono, sal_id)
VALUES (21766717, '8', 'Renata', 'Ignacia', 'Améstica', 'Hernández',TO_DATE('19-07-2005', 'DD-MM-YYYY'), 412268601, 110);

-- 3. Cambiamos el sistema de salud de paciente Renata Améstica.
UPDATE PACIENTE
SET sal_id = 100
WHERE pac_run = 21766717;