#Créer une fonction nommée « time_to_text » qui prend en paramètre un «nombre entier » de minutes 
#et « affiche en console » 
#une chaine de caractère sous la forme de : « X heures et Y minutes ».

def time_to_text(minute):
    if int(minute)==minute:
        print(minute)
    else : print("le nombre de minute n'est pas entier")
    if minute >= 60: hour = int(minute/60) # ou minute//60
    minuterestante= minute-int(hour)*60    # et minute%60
    print(hour,"heures et", minuterestante,"minutes")

time_to_text(140)
time_to_text(360)
time_to_text(545)