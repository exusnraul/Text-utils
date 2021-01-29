const change = document.getElementById('change');
const color = document.getElementById('color');

change.addEventListener('click', changebg);

function changebg() {
    const col1 = getrandomRGB();
    const col2 = getrandomRGB();
    const col3 = getrandomRGB();

    const colorstring = `rgb(${col1} , ${col2} , ${col3})`;
    // console.log(colorstring);
    document.body.style.background = colorstring;
    document.getElementById("color").textContent = colorstring;
}

function getrandomRGB() {
    return Math.floor(Math.random() * 256)
}