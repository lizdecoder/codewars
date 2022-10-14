// Your task is to find the first element of an array that is not consecutive.

// E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

// If the whole array is consecutive then return null.

// The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

// original attempt
// function firstNonConsecutive (arr) {
//     let nonConsecutive;
//     for (let i = 0; i < arr.length-1; i++){
//         let consecutive = arr[i] + 1;
//         if (consecutive !== arr[i+1]){
//             if(consecutive < arr[i+1]) {
//                 nonConsecutive = arr[i+1];
//                 return nonConsecutive
//             }
//         }
//         nonConsecutive = null;
//     }
//     return nonConsecutive;
// }
    
// refractored 
function firstNonConsecutive (arr) {
    for (let i = 0; i < arr.length-1; i++){
        let consecutive = arr[i] + 1;
        if (consecutive !== arr[i+1]){
            return arr[i+1]
        }
    }
    return null;
}
    

// num = firstNonConsecutive([1,2,3,4,6,7,8]); //6
// num = firstNonConsecutive([1,2,3,4,5,6,7]); //null
// num = firstNonConsecutive([1,9,3,4,5,6,7]); //9
num = firstNonConsecutive([1,2,3,4,5,6,7,10]); //10
console.log(num)