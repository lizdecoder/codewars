// Simple, remove the spaces from the string, then return the resultant string.

function noSpace(x) {
    return x.split(" ").join('');
}

// s = noSpace('8 j 8   mBliB8g  imjB8B8  jl  B')
// s = noSpace('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd')
s = noSpace('8aaaaa dddd r     ')
console.log(s)