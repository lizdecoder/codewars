// Count the number of divisors of a positive integer n.

// Random tests go up to n = 500000.

// Examples (input --> output)

// 4 --> 3 (1, 2, 4)
// 5 --> 2 (1, 5)
// 12 --> 6 (1, 2, 3, 4, 6, 12)
// 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)

function getDivisorsCnt(n){
    count = 0;
    for (let i = 1; i <= n; i++){
        if (!(n % i)){
            count++;
        }
    }
    return count;
}

c = getDivisorsCnt(1); //1
// c = getDivisorsCnt(10); //4
// c = getDivisorsCnt(11); //2
// c = getDivisorsCnt(54); //8

console.log(c);