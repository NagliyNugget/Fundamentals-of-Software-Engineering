def read_protein_data(filename):
    proteins = []
    file=open(filename,'r', encoding='utf-8')
    for line in file:
        line=line.strip()
        parts=line.split('\t')
        protein_data = (
            parts[0].strip(),
            parts[1].strip(),
            parts[2].strip(),
        )
        proteins.append(protein_data)
    return proteins

proteins=read_protein_data('sequences.0.txt')
for i, protein in enumerate(proteins, 1):
    name, organism, sequence = protein
    print(f"Белок {i}:")
    print(f" Название: {name}")
    print(f" Организм: {organism}")
    print(f" Аминокислоты: {sequence}")
