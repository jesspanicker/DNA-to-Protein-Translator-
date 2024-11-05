import random
import os
genetic_code = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
def translate_dna_to_protein(dna_sequence):
    protein_sequence = ""
    for i in range (0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid == '*': #stop codon
                break
            protein_sequence += amino_acid
        else:
            protein_sequence += 'X' #unknown codon
    return protein_sequence

#generate 10 random DNA sequences of 200 base pairs
random.seed(42) #reproducibilty
dna_sequences = [''.join(random.choices('ATGC', k=200)) for _ in range(10)]

# current working directory
current_dir = os.getcwd()

# write sequences to fasta file in the current directory
#print output
file_path = os.path.join(current_dir, "sequences.fasta")
with open(file_path, "w") as fasta_file:
    for i, dna_seq in enumerate(dna_sequences, 1):
        protein_seq = translate_dna_to_protein(dna_seq)
        fasta_file.write(f">DNA_Sequence_{i}\n{dna_seq}\n")
        fasta_file.write(f">Protein_Sequence_{i}\n{protein_seq}\n")
        print(f"DNA Sequence {i}: {dna_seq}")
        protein_seq = translate_dna_to_protein(dna_seq)
        print(f"Translated Protein Sequence {i}: {protein_seq}\n")


