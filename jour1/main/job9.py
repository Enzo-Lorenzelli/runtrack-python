nom, prix, stock,ajout=("nom_produit", 15, 50,100)
demande_utilisateur=int(input("entrer le nombre de produit à acheter"))
stockajout=(stock+ajout)
stockfinal=(stockajout-demande_utilisateur)
inflation=(1.1)
prixinflation=(prix*inflation)
print(f"le prix de {nom} est de {prix} il reste en stock : {stock}")
print("information sur le produit")
print("produit :",(nom))
print("Prix unitaire :",(prix))
print("quantité en stock", (stock))

print("stock après ajout",(stockajout))
print("le prix à l'unité aprés l'inflation est de :",(prixinflation))

print(f"le prix de {nom} est de {prix*inflation} après l'inflation de 10%")
print(f"l'utilisateur achète 30 {nom} pour une valeur de {prixinflation*30} il reste en stock {stockfinal}")

print("aprés achat et inflation")
print(f"le prix de {nom} est de {prixinflation} il reste en stock : {stockfinal}")
print("information sur le produit")
print("produit :",(nom))
print("Prix unitaire :",(prixinflation))
print("quantité en stock", (stockfinal))