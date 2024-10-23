def mainFunction() :
    entree = input("Entrez une opération :")
    if "+" in entree :
        operation = '+'
        operandes = entree.split('+')
    elif "-" in entree :
        operation = '-'
        operandes = entree.split('-')
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

    if operation == '+' :
        pass
    elif operation == '-' :
        pass
    elif operation =='*' :
        pass
    elif operation =='/' :
        pass
    else :
        print("Operation inconnue.")