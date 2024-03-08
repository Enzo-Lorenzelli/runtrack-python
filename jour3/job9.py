#ne pas utiliser range dans cette situation car range génére des sequences

def moyenne(note1,note2,note3):
    moyenne_etudiant=((note1+note2+note3)/3)
    print (moyenne_etudiant)
    if   0 <= moyenne_etudiant <= 7.999: #.999 ajouter pour que la plage ne soit pas vide entre 7 et 8
        print("Élève devant faire des efforts si la moyenne est comprise entre 0 et 7.")
    elif 8 <= moyenne_etudiant <= 10.999: #.999 ajouter pour que la plage ne soit pas vide entre 10 et 11
        print("Élève moyen si la moyenne est comprise entre 10 et 8.")
    elif 11 <= moyenne_etudiant <= 14.999: #.999 ajouter pour que la plage ne soit pas vide entre 14 et 15
        print("Bon élève si la moyenne est comprise entre 14 et 11.")
    elif 15 <= moyenne_etudiant <= 20:
        print("Très bon élève si la moyenne est comprise entre 20 et 15.")
    else: 
        if -0.0001>moyenne_etudiant or moyenne_etudiant>20: #empeche la note d'etre inferieur à 0 ou superieur à 20
            print("la moyenne doit etre comprise entre 0 et 20")

moyenne(10,8,14)
moyenne(15.3,14,15.5)
moyenne(0,15,4)
moyenne(20,20,19)
moyenne(100,129,48)