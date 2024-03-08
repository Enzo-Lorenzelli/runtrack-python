#Écrire un programme qui calcule le produit de toutes les valeurs de la liste comprises dans l’intervalle [25, 90].
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
produit=1
def calcul():
    global produit
    for element in L:
        if 25<= element <= 90:
            produit=produit*element
            print(produit)
calcul() #1x27=27 27x48=1296 1296x84=108864