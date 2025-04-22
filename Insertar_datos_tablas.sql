-- administrativos --
INSERT INTO E11EVENSTORE_ADMINISTRATIVOS (RUT,NOMBRE,APELLIDOS,USUARIO,EMAIL,CLAVE,FECHANACIMIENTO,DIRECCION) 
VALUES ('11555888-1','MARIA','DONOSO','MA.DONOSO','MA.DONOSO@GMAIL.COM','MA.DONOSO123',TO_DATE('17/04/85','DD/MM/RR'),'LAS LILAS 24, FLORIDA');

-- clientes --
INSERT INTO E11EVENSTORE_CLIENTES (RUT,NOMBRE,APELLIDOS,USUARIO,EMAIL,CLAVE,FECHANACIMIENTO,DIRECCION) VALUES ('24555444-3','DANIEL','MUNOZ','DANIEL21','DA.MUNOZ@GMAIL.COM','DANIEL123',TO_DATE('17/04/99','DD/MM/RR'),NULL);

INSERT INTO E11EVENSTORE_CLIENTES (RUT,NOMBRE,APELLIDOS,USUARIO,EMAIL,CLAVE,FECHANACIMIENTO,DIRECCION) VALUES ('15801477-5','Alejandra Camila','Nuñez Gilberto','Alejandra2105','alejandra.nu@gmail.com','Alejandra2105',TO_DATE('21/05/91','DD/MM/RR'),'Catedral 1310, depto 101, Santiago');

INSERT INTO E11EVENSTORE_CLIENTES (RUT,NOMBRE,APELLIDOS,USUARIO,EMAIL,CLAVE,FECHANACIMIENTO,DIRECCION) VALUES ('16801477-5','ALEJANDRA','PEREZ','ALEJANDRA22','ALEJAPE@GMAIL.COM','A123456',TO_DATE('19/04/95','DD/MM/RR'),'CALLE LAS CALILAS 55');

INSERT INTO E11EVENSTORE_CLIENTES (RUT,NOMBRE,APELLIDOS,USUARIO,EMAIL,CLAVE,FECHANACIMIENTO,DIRECCION) VALUES ('10316874-8','MANUEL','GUERRERO','MANUEL55','DANI_GUERRERO@GMAIL.COM','D123456',TO_DATE('08/09/89','DD/MM/RR'),NULL);

-- compras --
INSERT INTO E11EVENSTORE_COMPRA (NUMERO_COMPRA,DIRECCION_ENVIO,METODO_PAGO,FECHA,ESTADO,CLIENTE_ID) 
VALUES ('E11-382719','Catedral 202','transferencia',TO_TIMESTAMP('20/04/25 19:05:57,172076000','DD/MM/RR HH24:MI:SSXFF'),'Pendiente','16801477-5');

INSERT INTO E11EVENSTORE_COMPRA (NUMERO_COMPRA,DIRECCION_ENVIO,METODO_PAGO,FECHA,ESTADO,CLIENTE_ID) 
VALUES ('E11-799891','catedral 210','tarjeta_credito',TO_TIMESTAMP('20/04/25 19:21:18,910546000','DD/MM/RR HH24:MI:SSXFF'),'Pendiente','16801477-5');

INSERT INTO E11EVENSTORE_COMPRA (NUMERO_COMPRA,DIRECCION_ENVIO,METODO_PAGO,FECHA,ESTADO,CLIENTE_ID) 
VALUES ('E11-594063','Catedral 1310, depto 101, Santiago','gift_card',TO_TIMESTAMP('20/04/25 17:59:35,670980000','DD/MM/RR HH24:MI:SSXFF'),'Pendiente','16801477-5');

INSERT INTO E11EVENSTORE_COMPRA (NUMERO_COMPRA,DIRECCION_ENVIO,METODO_PAGO,FECHA,ESTADO,CLIENTE_ID) 
VALUES ('E11-593551','CASA1','transferencia',TO_TIMESTAMP('20/04/25 19:33:39,121112000','DD/MM/RR HH24:MI:SSXFF'),'Pendiente','16801477-5');

INSERT INTO E11EVENSTORE_COMPRA (NUMERO_COMPRA,DIRECCION_ENVIO,METODO_PAGO,FECHA,ESTADO,CLIENTE_ID) 
VALUES ('E11-831388','Calle las lelas 23','transferencia',TO_TIMESTAMP('21/04/25 00:32:40,829507000','DD/MM/RR HH24:MI:SSXFF'),'Pendiente','16801477-5');

-- detalles de compra --
INSERT INTO E11EVENSTORE_DETALLECOMPRA (CANTIDAD,COMPRA_ID,PRODUCTO_ID) 
VALUES ('1','21','50');
INSERT INTO E11EVENSTORE_DETALLECOMPRA (CANTIDAD,COMPRA_ID,PRODUCTO_ID) 
VALUES ('1','22','48');
INSERT INTO E11EVENSTORE_DETALLECOMPRA (CANTIDAD,COMPRA_ID,PRODUCTO_ID) 
VALUES ('2','23','50');
INSERT INTO E11EVENSTORE_DETALLECOMPRA (CANTIDAD,COMPRA_ID,PRODUCTO_ID) 
VALUES ('1','21','25');
INSERT INTO E11EVENSTORE_DETALLECOMPRA (CANTIDAD,COMPRA_ID,PRODUCTO_ID) 
VALUES ('1','24','50');
INSERT INTO E11EVENSTORE_DETALLECOMPRA (CANTIDAD,COMPRA_ID,PRODUCTO_ID) 
VALUES ('1','41','50');

-- Productos --
INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Need For Speed Unbound','20990','CAT_1-Carreras','https://www.todojuegos.cl/Productos/_mediaProd/29406/nfsunbucfhico.jpg','9','sta última adición a la franquicia Need for Speed de Criterion Games ofrece campañas de un jugador y multijugador, con carreras electrizantes llenas de adrenalina');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Assassins Creed Mirage','49990','CAT_5-Accion','https://m.media-amazon.com/images/I/81XTMj3qhPL._SL1500_.jpg','9','En esta ocasion encarnamos a Basim, un joven ladron callejero al que acompañamos en su periplo para convertirse en un maestro de los Asesinos. Desarrollado por Ubisoft Bordeaux, su historia nos lleva a la ciudad de Bagdad del siglo IX, para descubrir nuestro pasado y acabar con la amenaza de los miembros de la Orden que controlan la ciudad');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Street Fighter 6','39990','CAT_5-Accion','https://preview.redd.it/street-fighter-6-box-art-leaked-v0-33j6wl0xpr4a1.png?auto=webp&s=8088b280bf4f255c5677bdc438484da0cbbff20c','6','Por primera vez, SF6 ofrece una experiencia narrativa inmersiva en constante evolucion que le da poder al jugador para crear su propio Guerrero Mundial y participar verdaderamente en el Universo Street Fighter. SF6 proporciona la experiencia de lucha estandar para que los profesionales tanto ocasionales como probados en batalla puedan disfrutar en los años venideros');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('The Crew Motorfest','59990','CAT_1-Carreras','https://cdn.mobygames.com/covers/17647229-the-crew-motorfest-playstation-5-front-cover.jpg','4','Compite en carreras emocionantes y eventos temáticos en este paraíso automovilístico con cientos de vehículos legendarios');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Counter Strike','0','CAT_4-Free to play','https://shared.fastly.steamstatic.com//store_item_assets/steam/apps/1222670/4bcb26e78354f1789d2af48258e9054dd3ca5043/capsule_616x353_alt_assets_7_spanish.jpg?t=1740506448','10','Durante las dos últimas décadas, Counter Strike ha proporcionado una experiencia competitiva de primer nivel para los millones de jugadores de todo el mundo que contribuyeron a darle forma.');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Sims 4','0','CAT_4-Free to play','https://shared.fastly.steamstatic.com//store_item_assets/steam/apps/1222670/4bcb26e78354f1789d2af48258e9054dd3ca5043/capsule_616x353_alt_assets_7_spanish.jpg?t=1740506448','10','¡Crea un mundo único de Sims a tu imagen y semejanza! Crea y personaliza Sims, construye casas increíbles y juega a la vida. Amplía tu juego con packs y kits para descubrir más moda, decoración, profesiones y más.');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Monster Hunter World','25990','CAT_3-Mundo abierto','https://http2.mlstatic.com/D_NQ_NP_897318-MLU70059888000_062023-O.webp','5','Monster Hunter World es el retorno de la serie a las consolas de sobremesa, permitiéndonos cazar criaturas gigantes en un entorno salvaje, ya sea en solitario o con tres cazadores con un nuevo sistema multijugador drop-in que permite cooperativo entre regiones');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Grand Theft Auto V','19990','CAT_3-Mundo abierto','https://juegosdigitaleschile.com/files/images/productos/1538762676-grand-theft-auto-5-gta-v-gta-5-ps4-primaria-solo-por-hoy.jpg','18','Esta versión del éxito, más ambiciosa técnicamente, presenta gráficos y nuevo contenido como armas, vehículos o misiones, además de una banda sonora ampliada y más jugadores en el modo online');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('For Honor','25990','CAT_6-Supervivencia','https://juegospro.cl/cdn/shop/files/eb380427-9371-4daa-9675-75a6d71c8497.jpg?v=1728033747&width=1445','9','Ubisoft presenta con For Honor un videojuego medieval con especial énfasis en la cooperación entre varios jugadores por equipos, que destaca por sus violentos combates y poderoso apartado gráfico');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Fortnite: Darkfire Bundle Switch','19990','CAT_6-Supervivencia','https://m.media-amazon.com/images/I/5177HgzL1NL._AC_UF1000,1000_QL80_.jpg','13','Fortnite es un videojuego de Epic Games que nos transporta a un mundo sandbox donde explorar, construir y sobrevivir a los peligros de la noche.');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Resident Evil Revelations','19990','CAT_2-Terror','https://juegosdigitaleschile.com/files/images/productos/1503962921-resident-evil-revelations-p4.JPG','10','Resident Evil: Revelations —cuyo título original en Japón es Biohazard: Revelations —es un videojuego de terror y supervivencia de disparos en tercera persona desarrollado y publicado por Capcom y lanzado originalmente en 2012 para la consola portátil Nintendo 3DS.');

INSERT INTO E11EVENSTORE_PRODUCTO (NOMBRE,PRECIO,CATEGORIA,IMAGEN,STOCK,DESCRIPCION) 
VALUES ('Silent Hill 2 PS5','55990','CAT_2-Terror','https://i.postimg.cc/wj8pD0h9/preferable-box.jpg','5','Un remake del SILENT HILL 2 de 2001 con nuevos gráficos de avanzada que incluyen trazado de rayos. Mira el perturbador mundo de Silent Hill como nunca antes, y disfruta de una experiencia narrativa aún más inmersiva. ');

-- transaccion pagos --
INSERT INTO E11EVENSTORE_TRANSACCIONPAGO (METODO_PAGO,ESTADO,MONTO,FECHA_TRANSACCION,CODIGO_AUTORIZACION,COMPRA_ID) 
VALUES ('transferencia','completado','23980',TO_TIMESTAMP('21/04/25 00:32:41,020856000','DD/MM/RR HH24:MI:SSXFF'),NULL,'41');