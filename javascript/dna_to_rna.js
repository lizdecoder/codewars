// Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

// Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

// Create a function which translates a given DNA string into RNA.

// For example:

// "GCAT"  =>  "GCAU"

dna = "TTTT"
// dna = 'GCAT'

// first attempt
// function DNAtoRNA(dna){
// 	for(acid of [...dna]){
// 		dna = dna.replace('T','U')
// 	}
// 	return dna
// }

// refractored
function DNAtoRNA(dna) {
	return dna.replace(/T/g, 'U')
}


d = DNAtoRNA(dna);
console.log(`at call ${d}`);