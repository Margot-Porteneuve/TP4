import numpy as np
# Exercice 1 : Polynomes 
# 1

def afficher(p):
    """
    Cette fonction affiche le polynome p sous la forme"anX^n+...+a0
    @param p: polynôme d'entrée
    """
    print("Polynome = ",end="")
    a=0
    n=len(p)-1
    for i in range(n,0,-1):
        a=p[i]
        print(f"{a}X^{i}",end="")
        print("+",end="")
    print(p[0])
    return

def get_valeur(p,x):
    """
    Cette fonction calcul et renvoie la valeur du polynome p au point x
    @param p : polynome en entrée
    @param x : valeur en entrée à remplacer dans le polynome
    @return res polynome calculer au point x
    """
    res=p[0]
    for i in range(1,len(p)):
        res+=p[i]*(x**i)
    return res

def deriver(p):
    """
    Cette fonction calcul et renvoie la dérivé du polynome
    @param p : polynome en entrée
    @return deriv: dériver du polynome
    """
    deriv = []
    for i in range(1,len(p)):
        deriv.append(p[i]*i)
    return deriv

# Test des fonctions supérieurs
def test ():
    p = [4,3,2,1]
    x = 2
    # En calcul : 
    # afficher = X^3 + 2*X^2 + 3*X + 4
    # get_valeur = 26
    # deriver = [3,4,3] -> affiche(deriver(p))= 3*X^2 + 4*X + 3
    afficher(p)
    print(get_valeur(p,x))
    deriver(p)
    afficher(deriver(p))

#test()