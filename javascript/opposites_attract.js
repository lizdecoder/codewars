// Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

// Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

// const flower1 = 1
// const flower2 = 4
// flower1 = 2
// flower2 = 2
flower1 = 0
flower2 = 1
// flower1 = 0
// flower2 = 0

// original attempt
// function lovefunc(flower1, flower2){
// 	sum = flower1 + flower2;
// 	if (sum % 2 !== 0) return true;
// 	return false;
// }

// second attempt
function lovefunc(flower1, flower2){
	return (flower1+flower2) % 2 !== 0;
}

love = lovefunc(flower1, flower2)
console.log(love)