function loadImage(url) {
    return new Promise(resolve => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.responseType = "blob";
        xhr.onload = function (e) {
            const reader = new FileReader();
            reader.onload = function(event) {
                const res = event.target.result;
                resolve(res);
            }
            const file = this.response;
            reader.readAsDataURL(file);
        }
        xhr.send();
    });
}

let signaturePad = null;

window.addEventListener('load', async () => {

    const canvas = document.querySelector("canvas");
    canvas.height = canvas.offsetHeight;
    canvas.width = canvas.offsetWidth;

    signaturePad = new SignaturePad(canvas, {});

    const form = document.querySelector('#form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
    
        let curso = document.getElementById('curso').value;
        let apellidoPaterno = document.getElementById('apellidoPaterno').value;
        let apellidoMaterno = document.getElementById('apellidoMaterno').value;
        let nombres = document.getElementById('nombre').value;
        let direccion = document.getElementById('direccion').value;
        let telefono = document.getElementById('telefono').value;
        let email = document.getElementById('email').value;
        // let hijos = document.querySelector('input[name="hijos"]:checked').value;
        // let numeroHijos = document.getElementById('numeroHijos').value;
        let enfermedad = document.querySelector('input[name="enfermedad"]:checked').value;
        let enfermedadDesc = document.getElementById('enfermedad-desc').value;
        let discapacidad = document.querySelector('input[name="discapacidad"]:checked').value;
        let discapacidadDesc = document.getElementById('discapacidad-desc').value;

        generatePDF(curso, apellidoPaterno, apellidoMaterno, nombres, direccion, telefono, email, enfermedad, enfermedadDesc, discapacidad, discapacidadDesc);
    })

});

async function generatePDF(curso, apellidoPaterno, apellidoMaterno, nombres, direccion, telefono, email, enfermedad, enfermedadDesc, discapacidad, discapacidadDesc) {
    const image = await loadImage("formulario.jpg");
    const signatureImage = signaturePad.toDataURL();

    const pdf = new jsPDF('p', 'pt', 'letter');

    pdf.addImage(image, 'PNG', 0, 0, 565, 792);
    pdf.addImage(signatureImage, 'PNG', 190, 400, 300, 60);

    pdf.setFontSize(12);
    pdf.text(curso, 145, 130);

    const date = new Date();
    pdf.text(date.getUTCDate().toString(), 135, 155);
    pdf.text((date.getUTCMonth() + 1).toString(), 175, 155);
    pdf.text(date.getUTCFullYear().toString(), 220, 155);

    pdf.setFontSize(10);
    pdf.text(apellidoPaterno, 170, 200);
    pdf.text(apellidoMaterno, 170, 213);
    pdf.text(nombres, 170, 225);
    pdf.text(direccion, 170, 240);
    pdf.text(telefono, 170, 253);
    pdf.text(email, 170, 264);

    pdf.setFillColor(0,0,0);

    if (parseInt(discapacidad) === 0) {
        pdf.circle(241, 326, 4, 'FD');
    } else {
        pdf.circle(205, 328, 4, 'FD');
        pdf.text(discapacidadDesc, 290, 330);
    }

    if (parseInt(enfermedad) === 0) {
        pdf.circle(241, 367, 4, 'FD');
    } else {
        pdf.circle(205, 368, 4, 'FD');
        pdf.text(enfermedadDesc, 290, 370);
    }




    pdf.save("TRAVEL SAFE.pdf");

}