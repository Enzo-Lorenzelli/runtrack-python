L=[2,5,7,8,9]
def lecture():
    print (L)
    print(L[1:2])
    addition=L[2]+L[4]
    print(addition, "Test")
    L[3]=addition #ou à la place d'addition : L[3]=L[2]+L[4]
    print(L)
    print(L[4:5])
lecture()