#Saisie de la matrice:

graphe = [
        [0,-1,4,float("Inf"),float("Inf")],
        [float("Inf"),0,3,2,2],
        [float("Inf"),float("Inf"),0,float("Inf"),float("Inf")],
        [float("Inf"),1,5,0,float("Inf")],
        [float("Inf"),float("Inf"),float("Inf"),-3,0]
    ]

#Application de l'algorithme de Bellman:

def Algorithme_Bellman(graphe, point_source):
    distances = [float("Inf")] * len(graphe)
    distances[point_source] = 0
    for a in range(len(graphe) - 1):
        for x in range(len(graphe)):
            for y in range(len(graphe)):
                if distances[x] + graphe[x][y] < distances[y]:
                    distances[y] = distances[x] + graphe[x][y]

    for x in range(len(graphe)):
        for y in range(len(graphe)):
            if distances[x] + graphe[x][y] < distances[y]:
                print("Le graphe contient un cycle négatif ! ")
                return
    return distances

#Resultat:

distances = Algorithme_Bellman(graphe, 0)
print("Resultat : ")
print("Distances depuis la Source")
for i in range(len(distances)):
        print("Sommet",i," : \t----->\t", distances[i])

