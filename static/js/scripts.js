document
  .getElementById("formulario")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var campo = document.getElementById("subscribe_contact").value;
    var emailRegex = /\S+@\S+\.\S+/;
    var mobileRegex = /^[+]?\d{1,3}[-\.\s]?\d{2,3}[-\.\s]?\d{3}[-\.\s]?\d{4}$/;

    if (emailRegex.test(campo)) {
      // El campoes un correo electrónico
      this.submit(); // Envía el formulario si la validación es exitosa
    } else if (mobileRegex.test(campo)) {
      // El campo es un número de teléfono móvil
      this.submit(); // Envía el formulario si la validación es exitosa
    } else {
      // El campo no es un correo electrónico ni un número de teléfono móvil válido
      alert(
        "El campo debe ser un correo electrónico o un número de teléfono móvil válido"
      );
    }
  });
