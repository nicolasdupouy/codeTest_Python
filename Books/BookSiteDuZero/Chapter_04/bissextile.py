#!/usr/bin/python3
# -*-coding:Latin-1 -*
#import os
#print("Hello the world !")
#input("Press enter to close this program ...")
#os.system("sleep 5")

annee = input("Entrez l\'ann�e � tester:")
annee = int(annee)

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("""L'ann�e saisie est bissextille.""")
else:
    print("""L'ann�e saisie n'est pas bissextille.""")
        
#print("ann�e : ", annee)