from soustraction import soustraction
from division import division


def mainFunction() :
    entree = input("Entrez une opération :")
    if "+" in entree :
        operation = '+'
        operandes = entree.split('+')
    elif "-" in entree :
        operation = '-'
        operandes = entree.split('-')
        print(operandes)
    if "/" in entree :
        operation = '/'
        operandes = entree.split('/')
    elif "*" in entree :
        operation = '*'
        operandes = entree.split('*')
    else :
        print("Operation non authorisée.")
        return
    
    if len(operandes) !=2:
        print("Operation inconnue.")
        return

    left = float(operandes[0])
    right = float(operandes[1])
    print(left)

    if operation == '+' :
        pass
    elif operation == '-' :
        soustraction(left, right)
    elif operation =='*' :
        pass
    elif operation =='/' :
        division(left, right)
    else :
        print("Operation inconnue.")