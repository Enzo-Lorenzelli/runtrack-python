def verificator(number):
    print(number)
    if number < 0:
        print("n'est pas positif")
    else: print("positif")
    if int(number)==number: #convertie number en entier et vérifie si egaux à number.
        print("entier")
    else:print("pas entier")
    if number%2 == 0:
        print("pair")
    else:
        print ("impair")

verificator(-3)
verificator(1.5)
verificator(10)