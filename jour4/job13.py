i=0
def doublon():
    global i
    L=[10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    for element in L:
        if L[i]==len(L):
           del len(L[i+1])
           print(L)
           i+=1

doublon()