def croissant():
    L = [3, 6, 5, 9, 12, 8, 1, 0]
    for element in L:
        mini = L.index(min(L))
        maxi = L.index(max(L))
        L[0],L[mini] = L[mini],L[0]
        L[7],L[maxi] = L[maxi],L[7] 
    print (L)

croissant()

#     #Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.
# def croissant():
#     L = [3, 6, 5, 9, 12, 8, 1, 0]

#     for i in range(len(L) - 1):
#         if L[i] > L[i + 1]:
#                 L[i], L[i + 1] = L[i + 1], L[i]
#     print(L)

# croissant()



#expérience raté :

# x=0

# def croissant(L):
#     L=[3,6,5,9,12,8,1,0]
#     for element in L :
#         if L[x]!=L[8]:
#             if L[x]>L[x+1]:
#                 L[x], L[x+1] = L[x+1], L[x] #echanger de place si supérieur


# croissant()