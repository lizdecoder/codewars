// ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

// If the function is passed a valid PIN string, return true, else return false.

// Examples (Input --> Output)

// "1234"   -->  true
// "12345"  -->  false
// "a234"   -->  false

// original attempt
// function validatePIN (pin){
// /^-?\d+$/ all positive and negative whole numbers
// /^\d+$/ all positive whole numbers 
// '^([0-9]{4}|[0-9]{6})$' all positive numbers with length 4 or 6
// /^\d+\.\d+$/ all positive floats

//     if (pin.length === 4 || pin.length === 6) {
//         console.log("made it here")
//         return /^\d+$/.test(pin);
//     }
//     return false;
// }

// refractored
function validatePIN (pin){
    return /^(\d{4} | \d{6})$/.test(pin)
}

// bool = validatePIN("1234"); //true
// bool = validatePIN("12345"); //false
bool = validatePIN("a234"); //false
// bool = validatePIN('-1234') //false
// bool = validatePIN("-1.234") //false

console.log(bool);