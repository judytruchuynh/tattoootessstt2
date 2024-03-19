function convert() {
    var inch = parseFloat(document.getElementById("inchInput").value);
    var cm = inch * 2.54;
    document.getElementById("result").innerHTML = inch + " inches is equal to " + cm + " centimeters.";
}