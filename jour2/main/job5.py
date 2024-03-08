for nombre in range(0,101):
    if nombre % 5 == 0 and nombre % 3 == 0:
        print("fizzbuzz")
    if nombre % 3 == 0:
        print("fizz")
        if nombre % 5 == 0:
            print("buzz")
    else:
        print(nombre)