// You are given an odd-length array of integers, in which all of them are the same, except for one single number.

// Complete the method which accepts such an array, and returns that single different number.

// The input array will always be valid! (odd-length >= 3)

// Examples

// [1, 1, 2] ==> 2
// [17, 17, 3, 17, 17, 17, 17] ==> 3

// original attempt
// function stray(numbers) {
//     let sorted_arr = numbers.slice().sort();
//     console.log(`sorted arr: ${[sorted_arr]}`)
//     let unique_num = sorted_arr[0]
//     for (let i = 1; i < sorted_arr.length - 1; i++) {
//         if (unique_num == sorted_arr[i]){
//             if (unique_num != sorted_arr [i+1]){
//                 unique_num = sorted_arr [i+1]
//             }
//         }
//     }
//     return unique_num;
// }

// clever attempt
function stray(numbers) {
    for (let idx in numbers){
        console.log(numbers.indexOf(numbers[idx]), numbers.lastIndexOf(numbers[idx]))
        if (numbers.indexOf(numbers[idx]) === numbers.lastIndexOf(numbers[idx])) {
            return numbers[idx]
        }
    }
}


// num = stray([8, 2, 2]); //8 [2, 2, 8]
num = stray([ 1, 1, 1, 1, 1, 1, 0 ]); //0
// num = stray([1, 1, 2]); //2
// num = stray([17, 17, 3, 17, 17, 17, 17]); //3
// num = stray([ 8, 1, 1, 1, 1, 1, 1 ]) //8
console.log(num)

