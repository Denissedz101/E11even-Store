function mostrarOpcionesCuenta(btnId = "boton-cuenta", panelId = "opciones-cuenta") {
  const btn = document.getElementById(btnId);
  const panel = document.getElementById(panelId);

  if (!btn || !panel) return;

  btn.addEventListener("click", function (e) {
    e.stopPropagation();
    panel.classList.toggle("d-none");
  });

  document.addEventListener("click", function () {
    if (!panel.classList.contains("d-none")) {
      panel.classList.add("d-none");
    }
  });

  panel.addEventListener("click", function (e) {
    e.stopPropagation();
  });
}

document.addEventListener("DOMContentLoaded", function () {
  try {
    mostrarOpcionesCuenta();
    console.log("? JS ejecutado correctamente");
  } catch (err) {
    console.error("? Error en mostrarOpcionesCuenta:", err);
  }
});
