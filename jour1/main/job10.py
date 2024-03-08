investissement=int(input("votre investissement"))
taux_de_rendement_annuel=1.02
annee=int(input("temps passer après investissement nombre d'années"))
capital=5000
investissement_capital=investissement+capital
rendement_final=(investissement_capital*taux_de_rendement_annuel)*annee
argent_retiré=rendement_final*0.9

print("vous avez fait un gain de :",(argent_retiré-investissement_capital))