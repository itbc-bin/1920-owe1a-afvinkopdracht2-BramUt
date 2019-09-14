seq_path = input("FASTA path: ")
seq = open(seq_path)
sequentie = ""

for regel in seq:
    if ">" not in regel:
        sequentie += regel.rstrip()

nucleotide_A = "A"
nucleotide_C = "C"
nucleotide_G = "G"
nucleotide_T = "T"
nucleotide_N = "N"

print(sequentie)

aantal_A = sequentie.count(nucleotide_A)
aantal_C = sequentie.count(nucleotide_C)
aantal_G = sequentie.count(nucleotide_G)
aantal_T = sequentie.count(nucleotide_T)
aantal_N = sequentie.count(nucleotide_N)

totaal = aantal_A + aantal_C + aantal_G + aantal_T + aantal_N

procentCG = (aantal_C + aantal_G) / totaal *100

print("Aantal nucleotiden: " , totaal)
print("Aantal nucleotiden (A): " , aantal_A)
print("Aantal nucleotiden (C): " , aantal_C)
print("Aantal nucleotiden (G): " , aantal_G)
print("Aantal nucleotiden (T): " , aantal_T)
print("Aantal nucleotiden (N): " , aantal_N)
print("Percentage CG : " , round(procentCG,1) , "%")
