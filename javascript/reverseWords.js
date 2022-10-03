// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

// Examples

// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

// original solution
// function reverseWords(str){
//     new_s = "";
//     for(word of str.split(/(\s+)/)) {
//         new_s += word.split("").reverse().join("");
//     }
//     return new_s;
// }

// clever solution
function reverseWords(str){
    return str.split(' ').map( (word) => word.split("").reverse().join('')).join(' ');
}



input = reverseWords("This is an example!");
// input = reverseWords("double  spaces");
console.log(input);