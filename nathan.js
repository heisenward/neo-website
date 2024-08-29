const Input = document.getElementById("Input");
const Input1 = document.getElementById("Inpu1t");
const Submit = document.getElementById("Submit");

Submit.onclick = function()
{

let SS = Number(Input.value);
let CC = Number(Input1.value);


  if (isNaN(CC) || isNaN(SS)){
window.alert("those arent numbers silly")

console.log(`SS: ${typeof SS}: ${SS}`)
console.log(`CC: ${typeof CC}: ${CC}`)

}
let SSS = (Input.value);
let CCC = (Input1.value);

  if (SSS === "" && CCC === ""){

    window.alert("Heyyy theres no data here !1")}

if (Number(CC) || Number(SS) || SSS !== "" && CCC !== "" && !isNaN(CC) && !isNaN(SS)){
window.alert("THANKS")

console.log(`SS1: ${typeof SS}: ${SS}`)
console.log(`CC1: ${typeof CC}: ${CC}`)
}
}