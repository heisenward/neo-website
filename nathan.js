let SSN;
document.getElementById("button").onclick = function()
{ SSN = document.getElementById("input").value;
console.log(`SSN: ${typeof SSN} ${SSN}`);
  window.alert("Thank you!")
  checkSSN();
}
function checkSSN(){
  if (typeof SSN === 'undefined' || SSN === ''){
      window.alert("heeyyyy, theres no data here!");

     if (typeof SSN !== 'number' || isNaN(SSN) === true || typeof SNN === 'string'){
      window.alert("And it has to a number");}
      document.getElementById("KK").textContent = ("I willl be selling thiss!!")
  }
}

  let CC;
  document.getElementById("button2").onclick = function(){
    CC = document.getElementById("input2").value; 
    console.log(`Credit Card Number: ${typeof CC} ${CC}`);
    window.alert("Thank you!")
    checkCC();
}

function checkCC(){ 
  if (typeof CC === 'undefined' || CC === ''){
  window.alert("heeyyyy, theres no data here!");

 if (typeof CC !== 'number'|| isNaN(CC) === true){
window.alert("And its gotta be a number");
document.getElementById("KK").textContent = ("I willl be selling thiss!!")
}


    }
  }