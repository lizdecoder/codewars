// Complete the solution so that it reverses the string passed into it.

// example: 'world'  =>  'dlrow' 'word'   =>  'drow'

let str = 'word'

function reversed(str){
	return str.split("").reverse().join("");
}

s2 = reversed(str)
console.log(s2)