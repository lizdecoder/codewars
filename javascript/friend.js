// Make a program that filters a list of strings and returns a list with only your friends name in it.

// If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

// Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

// i.e.

// friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
// Note: keep the original order of the names in the output.

// original solution
// function friend(friends) {
//   trueFriends = [];
//   for (let name of [...friends]) {
//     if (name.length === 4) {
//       trueFriends.push(name);
//     }
//   }
//   return trueFriends;
// }

// clever solution
function friend(friends) {
    return friends.filter(name => name.length === 4)
}

f = friend(["Ryan", "Kieran", "Jason", "Yous"]);
console.log(f);
