exclus={26, 37, 88}
for nombre in (variable for variable in range(0,101) if variable not in exclus): #variable represente chaque element dans range s'il n'est pas dans la liste exclu.
    print (nombre)