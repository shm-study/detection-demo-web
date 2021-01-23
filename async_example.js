// Asyncronous Programming? 

// let order_num = 0;

// let order = function() { 
//     setTimeout(
//         function() {order_num = order_num + 1}
//     , 3000);
// }

// console.log(order_num);
// order()
// console.log(order_num);

// This source prints 0 two times 

// how to deal with async
// 1. callback (conventional): has limitations..
// 2. promise 
// 3. Async / Await 

function whatYourName(name, callback) { 
    console.log('name', name)
    setTimeout(
        function() {}
        , 3000);
        callback();
    );
}