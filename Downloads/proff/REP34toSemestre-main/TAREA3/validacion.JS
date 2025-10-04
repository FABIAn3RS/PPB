
function validarFormulario() {

    // obtener valores de los campos del formulario

    let nombre = document.getElementById("name_control").value;
    let apellido = document.getElementById("last_control").value;
    let email = document.getElementById("email_control").value;
    let cedula = document.getElementById("cedula_control").value;
    let password = document.getElementById("password_control").value;
    let nacimiento = document.getElementById("birthdate_control").value;
    let telefono = document.getElementById("tel_control").value;
    let direccion = document.getElementById("address_control").value;

    let listaformulario = [nombre, apellido, email, cedula, password, nacimiento, telefono, direccion];

    for (let element of listaformulario) {

        if (element.trim() == "") { alert("Por favor complete todos los campos"); return false; }
        console.log(element);
    }


    // validar fecha de nacimiento
    let completed = nacimiento.slice(0, 4);
    completed = Number(completed);
    if (completed < 1900 || completed > 2023) { alert("Año de nacimiento no válido"); return false; }
    console.log(completed);

    // validar cedula

    if (isNaN(cedula)) { alert("Cédula no válida"); return false; }
    console.log(cedula);

    alert("Formulario enviado con éxito");
    return true;
}