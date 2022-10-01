// Clock shows h hours, m minutes and s seconds after midnight.

// Your task is to write a function which returns the time since midnight in milliseconds.

// Example:

// h = 0
// m = 1
// s = 1

// result = 61000

function past(h, m, s){
    return h * 3_600_000 + m * 60_000 + s * 1_000;
}

// milli = past(0, 1, 1) //61000
// milli = past(1, 1, 1) //3661000
milli = past(0, 0, 0); //0

console.log(milli)