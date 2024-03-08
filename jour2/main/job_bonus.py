# 3 longueurs a, b, c
# triangle possible ? a + b > c    et   a + c > b     et      b + c > a
# si oui alors est ce un tri-rectangle, tri-isocèle, les deux ? et ou equilateral, quelquonque.
#triangle rectangle : si grand cote3 carré = coté1 + coté2

a=int(input("Entrez la longueur de a:"))
b=int(input("Entrez la longueur de b:"))
c=int(input("Entrez la longueur de c:"))


if a + b > c and a + c > b and b + c > a :
    print ("Triangle valide")
    abc=True
else :
    print ("triangle non valide")
    abc=False
if abc==True :
    if a==b==c :
        print ("triangle equilateral")
    else : print ("NON equilateral")
    if a==b or b==c or a==c :
        if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 :
            print ("Triangle Isocele Rectangle")
        else : print ("Triangle ISOCELE")
    else: print ("NON isocèle")
    if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 : 
         print("triangle rectange")
         if a==b or b==c or a==c :
             print ("triangle rectangle isocele")
         else : 
             print("NON triangle rectangle isocele")
    else :
        print ("NON rectangle")
#if else et print chaque etape.