const sub = document.getElementById("SUBMIT")
const input = document.getElementById("AAA")
const iii = document.getElementById("ii")
const H = document.getElementById("H")


sub.onclick = function fun(){
    
    const num1 = Number(input.value);
    let num = num1;

    if(isNaN(num1)){
      return  iii.textContent = `that isnt a valid number`;
   
    }
   while (num !== 1){
    if (num % 2 === 0){
        num = num / 2}

        else{ num = num * 3 + 1}
   }
             
    if (num == 1){

        {iii.textContent= `${num1} is a solution`;
    console.log(num)}

        if (num !== 1)
            {iii.textContent = `${num1} ISNT a solution`;
        console.log(num)}


    }
}
H.onclick = function(){

    input.value= ""
}