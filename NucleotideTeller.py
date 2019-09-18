#Vragen naar de path van het fasta bestand en zet de inhoud ervan in een variabele
seq_path = input("FASTA path: ")
seq = open(seq_path)
sequentie = ""

#Filteren line die bbeginnen met > en der whitespaces halen uit de rest
for regel in seq:
    if ">" not in regel:
        sequentie += regel.rstrip()

#Definiëren van de variabele voor iedere nucleotide
nucleotide_A = "A"
nucleotide_C = "C"
nucleotide_G = "G"
nucleotide_T = "T"
nucleotide_N = "N"

print(sequentie)

#Het tellen van het aantal nucleotide per soort
aantal_A = sequentie.count(nucleotide_A)
aantal_C = sequentie.count(nucleotide_C)
aantal_G = sequentie.count(nucleotide_G)
aantal_T = sequentie.count(nucleotide_T)
aantal_N = sequentie.count(nucleotide_N)

#Optellen totaal antal nucleotiden
totaal = aantal_A + aantal_C + aantal_G + aantal_T + aantal_N

#Percentage berekenen
procentCG = (aantal_C + aantal_G) / totaal *100

print("Aantal nucleotiden: " , totaal)
print("Aantal nucleotiden (A): " , aantal_A)
print("Aantal nucleotiden (C): " , aantal_C)
print("Aantal nucleotiden (G): " , aantal_G)
print("Aantal nucleotiden (T): " , aantal_T)
print("Aantal nucleotiden (N): " , aantal_N)
print("Percentage CG : " , round(procentCG,1) , "%")
