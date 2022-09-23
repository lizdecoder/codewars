// Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

// original attempt
// function even_or_odd(number) {
// 	if(number % 2 == 0){
// 		return 'Even'
// 	}
// 	return 'Odd'
// }

// refractored
function even_or_odd(number) {
	return number % 2 === 0 ? 'Even' : 'Odd'
}

even = even_or_odd(24)
odd = even_or_odd(37)

console.log(`24 is ${even}`)
console.log(`27 is ${odd}`)