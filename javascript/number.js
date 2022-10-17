// You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

// Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

// Take a look on the test cases.

// Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

// The second value in the first integer array is 0, since the bus is empty in the first bus stop.

// original
// var number = function(busStops) {
//     left = 0;
//     for(stop of busStops){
//         left += stop[0] - stop[1];
//     }
//     return left;
// }

// clever solution
// var number = function(busStops) {
//     return busStops.map(stop => stop[0] - stop[1]).reduce ( (firstStop, nextStop) => firstStop + nextStop);
// }

// clever solution
const number = busStops => busStops.reduce((prev, next) => prev + next[0] - next[1], 0) 

// people = number([[10,0],[3,5],[5,8]]) //5
// people = number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) //17
people = number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) //21
// people = number([[0,0]]) //0

console.log(people)