#Écrire un programme qui crée la liste d’entiers L = [7, 11, 42, 39, 2], votre programme 
#devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la liste.

def creation():
    L = [7, 11, 42, 39, 2]
    print("Liste d'entiers", L)
    L=[L[0]+1,L[1]+1,L[2]+1,L[3]+1,L[4]+1] #autre solution for x in range(len(L)): L[x]+=1
    print("liste +1 :", L)

creation()