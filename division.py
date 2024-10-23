def division(left:float, right:float)->float:
    """_summary_ return the result of left divided by right

    Args:
        left (float): _description_ float given by user
        right (float): _description_float given by user

    Returns:
        float: _description_ float
    """
    if left == 0 or right ==0:
        resultat = "Erreur, un des deux chiffres est égale à 0"
    else:
        resultat=left/right

    return resultat