L=[1,2,3,4,5]
def lecture():
    print(L,"initial")
    L[0], L[4] = L[4], L[0] #autre solution : variable temporaire pour stocker la valeur et l'echanger.
    print(L)

lecture()