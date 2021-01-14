const num = document.getElementById("number");
const dbl_btn = document.getElementById("double button");
const call_btn = document.getElementById("call button");

call_btn.addEventListener('click', call);
dbl_btn.addEventListener('click', double);

function double() { 
    alert("Double!");
    num.textContent = num.textContent*2
}

function call() { 
    alert("Call!");
    num.textContent = Number(num.textContent)+1
}


// alert(num.textContent);