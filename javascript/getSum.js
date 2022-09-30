// Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

// Note: a and b are not ordered!

// Examples (a, b) --> output (explanation)

// (1, 0) --> 1 (1 + 0 = 1)
// (1, 2) --> 3 (1 + 2 = 3)
// (0, 1) --> 1 (0 + 1 = 1)
// (1, 1) --> 1 (1 since both are same)
// (-1, 0) --> -1 (-1 + 0 = -1)
// (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

// original attempt
// function getSum (a, b) {
//     sum = 0;
//     if (a === b) {
//         return a;
//     }
//     if (b < a){
//         for (let i = b; i<=a; i++){
//             sum += i;
//         }
//     }else {
//         for (let i = a; i<=b; i++){
//             sum += i;
//         }
// }   
//     return sum;
// }

// clever attempt
function getSum (a, b) {
    return a > b ? getSum(b, a) : (b - a + 1) * (b + a) / 2
}

// sum = getSum(-1, 2);
// sum = getSum(1, 1);
// sum = getSum(1, 0);
// sum = getSum(1, 2);
// sum = getSum(0, 1);
// sum = getSum(-1, 0);
// sum = getSum(0, -1);
sum = getSum(568, -252);
console.log(sum)
