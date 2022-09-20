// Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

// my attempt but replacell() did not work on code wars
// function removeExclamationMarks(s) {
// 	s = s.replaceAll("!","")
// 	arr = s.split("")
// 	return arr
//   }

// my attempt
// function removeExclamationMarks(s) {
// 	return s.split("!").join("")
// }

// clever attempt
// 'g' = all occurances
// /and/ mark beginning and end of element
function removeExclamationMarks(s) {
	return s.replace(/!/g, "")
}

let str = removeExclamationMarks("hello!!")
console.log(str)