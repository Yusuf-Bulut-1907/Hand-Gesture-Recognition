"""
Ecrire une fonction qui calcule l'edit distance entre deux chaines de caracteres
Voir page 28 : D(s1, s2) = min(D(s1[1:], s2) + 1, D(s1, s2[1:]) + 1, D(s1[1:], s2[1:]) + (s1[0] != s2[0]))
"""

def edit_distance(s1, s2):
    matrice = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)] #initalisation de la matrice
    
    for i in range(len(s1) + 1):   #initialisation de la première colonne
        matrice[i][0] = i

    for j in range(len(s2) + 1):   #intialisation de la première ligne
        matrice[0][j] = j

    for k in range(1, len(s1) + 1):
        for l in range(1, len(s2) + 1):
            if s1[k-1] == s2[l-1]:     #si la lettre est égale => même valeur que la diagonale + pénalité (+0)
                matrice[k][l] = matrice[k-1][l-1]
            else: #si lettre différente => on prend le minimum des 3 chemins + pénalité (+1)
                matrice[k][l] = min(matrice[k-1][l], matrice[k][l-1], matrice[k-1][l-1]) + 1

    return matrice[len(s1)][len(s2)] #la distance d'édition est la valeur dans le coin inférieur droit de la matrice

# Test de la fonction
s1 = "1.56"
s2 = "1,56"

print(f"Edit distance entre '{s1}' et '{s2}' : {edit_distance(s1, s2)}")