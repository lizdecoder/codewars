// Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

// Examples (Input -> Output):

// * "String"      -> "SSttrriinngg"
// * "Hello World" -> "HHeelllloo  WWoorrlldd"
// * "1234!_ "     -> "11223344!!__  "

// my attempt
// function doubleChar(str){
// 	str = str.split("")
// 	new_str = []
// 	for (let i = 0; i < str.length; i++) {
// 		new_str.push(str[i])+new_str.push(str[i])
// 	}
// 	return new_str.join("")
// }

// clever solution
function doubleChar(str){
	return [...str].map(x => x.concat(x)).join("");
}

double = doubleChar("1234!_ ")
console.log(double)