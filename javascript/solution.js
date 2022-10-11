// Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

// original attempt
// function solution(str, ending){
//     console.log(str.length, ending.length)
//     return str.indexOf(ending, str.length - ending.length) !== -1;
// }

// clever attempt
function solution(str, ending){
    return str.endsWith(ending);
}    


// bool = solution('abc', 'bc') // returns true
bool = solution('abc', 'd') // returns false
console.log(bool)