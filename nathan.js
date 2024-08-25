
let me = "cool";

console.log("You are",me);

console.log(`You are ${me}`);

let NS = true;


console.log(`Theyre coming ${NS}`)

let H = 1111 

  console.log(typeof H);

//let bodies=200;
//bodies-= 1;
//console.log(bodies)
//let gamer= window.prompt("who are you?") 
//console.log(`He is ${gamer}`)

let SSN;
document.getElementById("button").onclick = function()
{ SSN = document.getElementById("input").value;
console.log(`SSN: ${SSN}`);
  window.alert("Thank you!")
  checkSSN();

}
function checkSSN(){
  if (typeof SSN === 'undefined' || SSN === ''){
      window.alert("heeyyyy, theres no data here!");}

    if (typeof SSN !== 'number' || isNaN(SSN)){
      window.alert("it has to a number silly!");
  }
  }


  let CC;
  document.getElementById("button2").onclick = function(){
    CC = document.getElementById("input2").value; 
    console.log(`Credit Card Number: ${CC}`);
    window.alert("Thank you!")
    checkCC();
}

function checkCC(){
if (typeof CC !== 'number' || isNaN(CC)){
window.alert("Its gotta be a number silly!");
}
 if (typeof CC === 'undefined' || CC === ''){
window.alert("heeyyyy, theres no data here!");
    }
  }

