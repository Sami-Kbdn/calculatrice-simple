
from soustraction import soustraction
from division import division

import addition as ad
import multiplication as mp


def mainFunction() :
    entree = input("Entrez une opération: ").replace(" ", "")
    if "+" in entree :
        operation = '+'
        operandes = entree.split('+')
    elif "-" in entree :
        operation = '-'
        operandes = entree.split('-')
    elif "/" in entree :
        operation = '/'
        operandes = entree.split('/')
    elif "*" in entree :
        operation = '*'
        operandes = entree.split('*')
    else :
        print("Operation non authorisée.")
        return
    
    #print(operandes)

    if len(operandes) !=2:
        print("Operation inconnue.")
        return

    left = float(operandes[0])
    right = float(operandes[1])
    print(left)

    resultat = 0

    if operation == '+' :
        resultat = ad.addition(left,right)
        print(f"le résultat est de : {resultat}")
    
    elif operation == '-' :
        resultat = soustraction(left, right)
        print(f"le résultat est de : {resultat}")

    elif operation =='*' :
        resultat = mp.multiplication(left,right)
        print(f"le résultat est de : {resultat}")

    elif operation =='/' :
        resultat = division(left, right)
        print(f"le résultat est de : {resultat}")
        
    else :
        print("Operation inconnue.")

    