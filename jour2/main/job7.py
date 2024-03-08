rows = "abcdefghijklmnopqrstuvwxyz"*10  # ou une autre chaîne de caractères représentant les lettres de l'alphabet

num_lines = len(range(0, len(rows), 20))  # déterminer le nombre de lignes en fonction de la longueur de la chaîne
for line in range(num_lines):   
    print(rows[line * 3: (line + 1) * 1]) #influe sur la longueur des 1ers lignes et le reste.

for i in range(num_lines):
    for j in range(i + 1):
        print(rows[j], end=' ')
    print('')