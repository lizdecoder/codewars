// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

// The output should be two capital letters with a dot separating them.

// It should look like this:

// Sam Harris => S.H

// patrick feeney => P.F

// original attempt
// function abbrevName(name){
//     initial = []
//     for (c of [...name.toUpperCase().split(" ")]){
//         console.log(`c: ${c} and charAt(0): ${c.charAt(0)}`)
//         initial.push(c.charAt(0))
//     }
//     string = initial[0] + "." + initial[1]
//     return string
// }

// clever solution
function abbrevName(name){
    return name.split(' ').map(i => i[0].toUpperCase()).join('.');
}

// initials = abbrevName("Sam Harris");
initials = abbrevName("patrick feeney");
console.log(initials);
