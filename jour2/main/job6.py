for number in range(2, 1001):  # Commencer à partir de 2 pour exclure le nombre 1
    if number == 2 or number == 3: #afficher 2 et 3 (exception pour le reste)
     print(number)
    if number % 2 != 0:  # Vérifie si le nombre n'est pas pair
        if number % 3 != 0:  # Vérifie si le nombre n'est pas divisible/multipliable par 3
            if number % 5 != 0:  # Vérifie si le nombre n'est pas divisible/multipliable par 5
                    print(number)
            else:
                pass  # Si le nombre est un multiple de 5, passe à l'itération suivante sans rien faire
        else:
            pass  # Si le nombre est un multiple de 3, passe à l'itération suivante sans rien faire
    else:
        pass  # Si le nombre est pair, passe à l'itération suivante sans rien faire

#essayer la commande continue.