def agriculture(type,saison):
    if type=="fruits" and saison=="hiver":
        print("orange, mandarine et kiwi")
    elif type=="fruits" and saison=="été":
        print("Poire, fraise, cassis")
    elif type=="légume" and saison=="hiver":
        print("carotte, topinambour, endive")
    elif type=="légume" and saison=="été":
        print("artichaut, aubergine,navet")

agriculture("fruits","hiver")
agriculture("fruits","été")
agriculture("légume","hiver")
agriculture("légume","été")