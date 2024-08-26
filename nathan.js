let SSN;
document.getElementById("button").onclick = function()
{ SSN = document.getElementById("input").value;
console.log(`SSN: ${SSN}`);
  window.alert("Thank you!")
  checkSSN();
document.getElementById("KK").textContent = ("I willl be selling thiss!!")
}
function checkSSN(){
  if (typeof SSN === 'undefined' || SSN === ''){
      window.alert("heeyyyy, theres no data here!");

    if (typeof SSN !== 'number' || isNaN(SSN)){
      window.alert("it has to a number silly!");}
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
  if (typeof CC === 'undefined' || CC === ''){
    window.alert("heeyyyy, theres no data here!");
 if (typeof CC !== 'number' || isNaN(CC)){
window.alert("Its gotta be a number silly!");
}


    }
  }