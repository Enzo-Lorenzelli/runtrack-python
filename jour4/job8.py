#Écrire un programme qui calcule la somme de toutes les valeurs paires:
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
somme=0
def calcul():
    global somme
    for element in L:
        if element % 2 ==0:
            somme=somme+element
            print(somme)

calcul()