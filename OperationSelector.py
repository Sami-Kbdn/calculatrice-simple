
import math

from soustraction import soustraction
from division import division

import addition as ad
import multiplication as mp
import modulo as md


def mainFunction() :
    #entree = input("Entrez une opération :")
    # if "+" in entree :
    #     operation = '+'
    #     operandes = entree.split('+')
    # elif "-" in entree :
    #     operation = '-'
    #     operandes = entree.split('-')
    # elif "/" in entree :
    #     operation = '/'
    #     operandes = entree.split('/')
    # elif "*" in entree :
    #     operation = '*'
    #     operandes = entree.split('*')
    # elif "%" in entree :
    #     operation = "%"
    #     operandes = entree.split("%")
    # else :
    #     print("Operation non authorisée.")
    #     return
    entree = ""
    print("operation> ",end='')
    while entree !='q' :
        entree = input().replace(" ", "")
        if entree =="q":
            return
        
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
        elif "%" in entree :
            operation = "%"
            operandes = entree.split("%")
        else :
            print("Operation non authorisée.")
            return
        
        #print(operandes)

        if len(operandes) !=2:
            print("Operation inconnue.")
            return

        left = float(operandes[0])
        right = float(operandes[1])

        resultat = math.inf

        if operation == '+' :
            resultat = ad.addition(left,right)        
        
        elif operation == '-' :
            resultat = soustraction(left, right)

        elif operation =='*' :
            resultat = mp.multiplication(left,right)

        elif operation =='/' :
            resultat = division(left, right)
        
        elif operation == "%":
            resultat = md.modulo(left,right)
        else :
            print("Operation inconnue.")

        if resultat != math.inf :
            print(f"le résultat est de : {resultat}")

        print()   
        print("operation> ",end='')
    
    print()   
    print("Au revoir")


    