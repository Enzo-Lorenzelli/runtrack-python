# job 4 solution #
#for i in range(1, 11):
    # nested loop #
    # to iterate from 1 to 10 #
#    for j in range(1, 11):
        # print multiplication #
#        print(i * j, end=' ')
#    print()

#alphabet = 'abcdefghijklmnopqrstuvwxyz' * 10
#for x in range(len(alphabet)):
#    for y in range(x+1):
#        print(alphabet.index(alphabet[y]), end="")
#    print()

#Chaine_de_caractere_vide=""
#triangle_rectangle="abcdefghijklmnopqrstuvwxyz"*10
#number=len(triangle_rectangle)
#for chaine in range(0,261):
#    if chaine==0:
#        print(triangle_rectangle)
#element_par_ligne=int(input("nombre de lettre par ligne"))
#Compteur_par_ligne=element_par_ligne+2
#for lettre in triangle_rectangle:
 #   print (triangle_rectangle range(0,element_par_ligne,260), end="")

#rickroll="YouknowtherulesandsodoIAfullcommitmentswhatImthinkingofYouwouldntgetthisfromanyotherguyIjustwannatellyouhowImfeelingGottamakeyouunderstandNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouWeveknowneachotherforsolongYourheartsbeenachingbutyouretooshytosayitInsidewebothknowwhatsbeengoingonWeknowthegameandweregonnaplayitAndifyouaskmehowImfeelingDonttellmeyouretooblindtoseeNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouOohGiveyouupOohoohGiveyouupOohoohNevergonnagivenevergonnagiveGiveyouupOohoohNevergonnagivenevergonnagiveGiveyouupWeveknowneachotherforsolongYourheartsbeenachingbutyouretooshytosayitInsidewebthknowwhatsbeengoingonWeknowthegameandweregonnaplayitIjustwannatellyouhowImfeelingGottamakeyouunderstandNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyou"
#for inner in range(len(1,rickroll,+1)):
#    for j in range(inner+1):
#        print(rickroll.index(rickroll[j]),end=" ")
#    print()

#rows = "YouknowtherulesandsodoIAfullcommitmentswhatImthinkingofYouwouldntgetthisfromanyotherguyIjustwannatellyouhowImfeelingGottamakeyouunderstandNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouWeveknowneachotherforsolongYourheartsbeenachingbutyouretooshytosayitInsidewebothknowwhatsbeengoingonWeknowthegameandweregonnaplayitAndifyouaskmehowImfeelingDonttellmeyouretooblindtoseeNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouOohGiveyouupOohoohGiveyouupOohoohNevergonnagivenevergonnagiveGiveyouupOohoohNevergonnagivenevergonnagiveGiveyouup"
# Séparer la chanson en lignes # Afficher chaque ligne de la chanson
#lines = [rows[i:i+30] for i in range(0, len(rows),1)]
#for line in lines:
#    print(line)
#for i in range(rows):
#    for j in range(i+1):
#        print(rows, end="")
#    print()
#rows = "YouknowtherulesandsodoIAfullcommitmentswhatImthinkingofYouwouldntgetthisfromanyotherguyIjustwannatellyouhowImfeelingGottamakeyouunderstandNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouWeveknowneachotherforsolongYourheartsbeenachingbutyouretooshytosayitInsidewebothknowwhatsbeengoingonWeknowthegameandweregonnaplayitAndifyouaskmehowImfeelingDonttellmeyouretooblindtoseeNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouNevergonnagiveyouupNevergonnaletyoudownNevergonnarunaroundanddesertyouNevergonnamakeyoucryNevergonnasaygoodbyeNevergonnatellalieandhurtyouOohGiveyouupOohoohGiveyouupOohoohNevergonnagivenevergonnagiveGiveyouupOohoohNevergonnagivenevergonnagiveGiveyouup"

# Diviser la chanson en lignes de 30 caractères et l'afficher
#lines = [rows[i:i+80] for i in range(0, len(rows), 1)]
#for line in lines:
#    print(line)
#
# Afficher la chanson sous forme de triangle
#for i in range(len(rows)):
#    for j in range(i + 1):
#        print(rows[j], end="")
#    print()

# a = int(input("Entrez la longueur de a:"))
# b = int(input("Entrez la longueur de b:"))
# c = int(input("Entrez la longueur de c:"))

# # Vérification de la validité du triangle
# if a + b > c and a + c > b and b + c > a:
#     print("Triangle valide")
#     abc = True
# else:
#     print("Triangle non valide")
#     abc = False

# # Identification du triangle isocèle rectangle
# if abc == True:
#     if a == b or b == c or a == c:
#         if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2:
#             print("Triangle isocèle rectangle")
#         else:
#             print("Triangle isocèle")
#     else:
#         print("NON isocèle")
# else:
#     print("NON triangle")

def dessiner_cercle(rayon):
    for y in range(-rayon, rayon+1):
        ligne = ''
        for x in range(-rayon, rayon+1):
            distance = x**2 + y**2
            if distance <= rayon**2:
                ligne += '* '  # Utilisez n'importe quel caractère ASCII que vous souhaitez pour représenter le cercle
            else:
                ligne += '  '  # Espace pour les points en dehors du cercle
        print(ligne)

# Test de la fonction avec un rayon de 10
dessiner_cercle(10)
