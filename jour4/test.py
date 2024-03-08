# def select_numbers():
#     numbers = []
#     print("Sélectionnez 5 nombres de 1 à 50, séparés par des espaces :")
#     while True:
#         user_input = input("Entrez les nombres : ")
#         user_numbers = user_input.split()
#         if len(user_numbers) != 5:
#             print("Veuillez entrer exactement 5 nombres.")
#         else:
#             valid = True
#             for num in user_numbers:
#                 if not num.isdigit() or not (1 <= int(num) <= 50):
#                     print("Veuillez entrer des nombres valides entre 1 et 50.")
#                     valid = False
#                     break
#             if valid:
#                 numbers = [int(num) for num in user_numbers]
#                 break
#     return numbers

# selected_numbers = select_numbers()
# print("Nombres sélectionnés :", selected_numbers)


# #Écrire un programme qui crée la liste d’entiers L = [7, 11, 42, 39, 2], votre programme 
# #devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la liste.

# total=0 

# number=[]

# def creation():
#     global total
#     while len(total)!=5: 
#         for x in range(len(50))
#     numberlist = [int(x) for x in creation]
#     print (numberlist)



# creation()

# def croissant(L):
#     # Déterminer la longueur de la liste
#     n = 0
#     for _ in L:
#         n += 1

#     # Tri à bulles
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if L[j] > L[j+1]:
#                 # Échanger les éléments
#                 L[j], L[j+1] = L[j+1], L[j]

#     return L

# # Liste d'entiers à trier
# L = [3, 6, 5, 9, 12, 8, 1, 0]

# # Appel de la fonction de tri et affichage du résultat
# print(croissant(L))