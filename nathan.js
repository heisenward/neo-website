/*
const Input = document.getElementById("Input");
const Input1 = document.getElementById("Inpu1t");
const Submit = document.getElementById("Submit");

let XXX = 0;

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


  if (SSS === "" && CCC === "" && XXX < 2){

    window.alert("Heyyy theres no data here !1")

    XXX ++;
  }

if (Number(CC) || Number(SS) || SSS !== "" && CCC !== "" && !isNaN(CC) && !isNaN(SS)){
window.alert("THANKS")

console.log(`SS1: ${typeof SS}: ${SS}`)
console.log(`CC1: ${typeof CC}: ${CC}`)
}
console.log(XXX)

if (XXX >= 2){
window.alert("uhhh steal nothing")
}
}


const email = "nathanbsmith0895@gmail.com"
let username = email.slice(0, email.indexOf("1 2 3 4 5 6 7 8 9 0 "))
console.log(username)
let email1 = email.slice( email.indexOf("1 2 3 4 5 6 7 8 9 0") )
console.log(email1)
let email_type =  email.slice( email.indexOf(" 1 2 3 4 5 6 7 8 9 0 ") + 1 )
console.log(email_type)
*/

///need to make it welcome only the name and not the numbers
const submit = document.getElementById("SUBMIT") 
const email = document.getElementById("EMAIL") 

submit.onclick = function(){

const emailVal = email.value;
const name2 = emailVal.slice(0, emailVal.indexOf(Number));
const name1 = emailVal.slice(0, emailVal.indexOf("@"));

const space = " "
const at = "@"
const error = document.getElementById("h33") 

  if (emailVal.includes(space)){
error.textContent = "space detected"
h1.textContent = `Welcome`;
  }

  if (!emailVal.includes(at)){
    error.textContent= "no @ symbol detected"
    h1.textContent = `Welcome`;
      }
      else{
      console.log("email:" ,email.value)

      console.log("name:" ,name1)

  const h1 = document.getElementById("WWWW")

  h1.textContent = `Welcome, ${name2}`;
  error.textContent= " ";}
};