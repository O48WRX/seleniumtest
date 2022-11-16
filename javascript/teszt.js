
function PrintFromScript() {
    document.getElementById("nameReturn").textContent = document.getElementById("name").value;
    document.getElementById("passReturn").textContent = document.getElementById("password").value;
    document.getElementById("ageReturn").textContent = document.getElementById("age").value;
}

function assessCalcs() {
    var a, b ,c ,d;
    a = document.getElementById("num1").value;
    b = document.getElementById("num2").value;
    c = document.getElementById("num3").value;
    d = document.getElementById("num4").value;
    document.getElementById("additionResult").textContent = parseInt(a) + parseInt(b);
    document.getElementById("subtractionResult").textContent = parseInt(c) - parseInt(d);
}
