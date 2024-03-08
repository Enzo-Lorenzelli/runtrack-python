def fruition():
    fruits=["pomme","cerise","orange","melon"]
    mangue=["mangue"]
    fruits = fruits[:2] + mangue + fruits[2:] #autre solution : mangue = "mangue" fruits.insert(2, mangue)
    print (fruits)

fruition()