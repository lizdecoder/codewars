// Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

// Example(Input => Output):

// 35231 => [1,3,2,5,3]
// 0 => [0]

// my original solution
function digitized(n) {
	// toString(10) = converts ints to string
	// split('') = splits string to individual parts
	// .map(Number) = loops through array and converts back to ints
	// reverse() = reverses array
	return n.toString(10).split('').map(Number).reverse();
}

// other solutions:
// function digitized(n) {
// 	return String(n).split('').map(Number).reverse()
// }

// function digitized(n) {
// 	return Array.from(String(n)), Number).reverse()
// }


n = digitized(35231)
console.log(n)