import addition as ad
import multiplication as mp
import modulo as md

def mainFunction() :
    entree = input("Entrez une opération :")
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
    
    #if len(operandes) !=2:
        #print("Operation inconnue.")
        #return

    left = float(operandes[0])
    right = float(operandes[1])

    resultat = 0

    if operation == '+' :
        resultat = ad.addition(left,right)
        print(f"le résultat est de : {resultat}")
    
    elif operation == '-' :
        pass
    elif operation =='*' :
        resultat = mp.multiplication(left,right)
        print(f"le résultat est de : {resultat}")

    elif operation =='/' :
        pass

    elif operation == "%":
        resultat = md.modulo(left,right)
        print(f"le résultat est de : {resultat}")
    else :
        print("Operation inconnue.")

    