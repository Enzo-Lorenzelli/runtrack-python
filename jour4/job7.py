L = [8, 24,48,2,16]
compteur=0
def trie():
        global compteur
        for element in L: 
              if element % 3 == 0:
                 compteur = compteur + 1 #ou compteur += 1
        print(compteur)
trie()