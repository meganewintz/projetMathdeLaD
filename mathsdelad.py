# -*- coding: ISO-8859-1 -*-

import random;
import numpy as np;

#Constantes de l'algo
nbre_eleves = 10
nbre_projets = 4
nbre_trinomes = nbre_eleves - nbre_projets*2
nbre_binomes = nbre_projets - nbre_trinomes
print "Nbre de binomes : %i  \nNbre de trinomes : %i\n" % (nbre_binomes, nbre_trinomes)

liste_eleves_restants = [i for i in range(nbre_eleves)]
liste_appreciations = ["TB", "B", "AB", "P", "I", "AR"]

matrice_pref = np.array([[random.choice(liste_appreciations) for j in range(nbre_eleves)] for i in range(nbre_eleves)])
matrice_proj = np.array([[random.choice(liste_appreciations) for p in range(nbre_projets)] for i in range(nbre_eleves)])
print "Tableau des appreciations élèves :\n", matrice_pref, "\n"
print "Tableau des appreciations projets :\n", matrice_proj, "\n"

def creerListeDesMentionsAcceptables(m):
	# permet de creer la liste de toutes les mentions supérieures ou égales à m

	liste_mentions_acceptables = []
	cpt = 0
	cherchem = True
	while cherchem:

		liste_mentions_acceptables.append(liste_appreciations[cpt])

		if liste_appreciations[cpt] == m:

			cherchem = False

		cpt += 1

	return liste_mentions_acceptables


def elevesAcceptesEntreEux(i, j, m):
	# données : i = i ème élève, j = j ème élève, m = mention minimale qu'il faut avoir entre les deux élèves
	# résultat : booléen; vrai si les élèves se sont mis mutuellement au moins la mention m, faux sinon

	resultat = False
	mentions_accept = creerListeDesMentionsAcceptables(m)

	if ((matrice_pref[i][j] in mentions_accept) and (matrice_pref[j][i] in mentions_accept)):

		resultat = True

	return resultat


# def elevesAcceptentMemeProjet(i, j, p, m):
# 	# données : i = i ème élève, j = j ème élève, p = numéro du projet auquel on s'intéresse,
# 	# m = mention minimale qu'il faut avoir de la part de chacun des élèves pour le projet p
# 	# résultat : booléen; vrai si les deux élèves ont au moins mis la mention m au projet p
#
# 	resultat = False
# 	mentions_accept = creerListeDesMentionsAcceptables(m)
#
# 	if ((matrice_proj[i][p] in mentions_accept) and (matrice_proj[j][p] in mentions_accept)):
#
# 		resultat = True
#
# 	return resultat

def eleveAccepteProjet(i, p, m):
	# données : i = i ème élève, p = numero du projet, m = mention mini que i doit avoir donnée pour p
	# résultat : booléen; vrai si i a au moins mis la mention m à p, faux sinon

	resultat = False
	mentions_accept = creerListeDesMentionsAcceptables(m)

	if (matrice_proj[i][p] in mentions_accept):

		resultat = True

	return resultat

def creerListeEleveInteresses(eleveRest, p, m):
	# données : eleveRest : liste des eleves qu'il reste à placer; p : numero du projet auquel on s interesse; m : mention minimale voulue, attribuée au projet p
	# resultat : liste des élèves (parmi les eleves qu il reste à placer) qui ont mis au moins la mention m à p

	resultat = []

	for i in eleveRest:

		if eleveAccepteProjet(i, p, m):

			resultat.append(i)

	return resultat

'''

# TESTS
print "mentions accept : ", creerListeDesMentionsAcceptables("AB")
"\n"
print "e2 a mis : ", matrice_pref[1][2], "a e3 \n"
print "e3 a mis : ", matrice_pref[2][1], "a e2 \n"
print elevesAcceptesEntreEux(2, 3, "TB")
"\n"
print elevesAcceptesEntreEux(2, 3, "B")
"\n"
print elevesAcceptesEntreEux(2, 3, "AB")
"\n"
print elevesAcceptesEntreEux(2, 3, "P")
"\n"
print elevesAcceptesEntreEux(2, 3, "I")
"\n"
print elevesAcceptesEntreEux(2, 3, "AR")
"\n"
"\n"
'''
'''
print "e3 a mis : ", matrice_proj[2][1], " au proj 2 \n"
print "e4 a mis : ", matrice_proj[3][1], " au proj 2 \n"
print elevesAcceptentMemeProjet(3, 4, 2, "TB")
"\n"
print elevesAcceptentMemeProjet(3, 4, 2, "B")
"\n"
print elevesAcceptentMemeProjet(3, 4, 2, "AB")
"\n"
print elevesAcceptentMemeProjet(3, 4, 2, "P")
"\n"
print elevesAcceptentMemeProjet(3, 4, 2, "I")
"\n"
print elevesAcceptentMemeProjet(3, 4, 2, "AR")
"\n"
'''

def main():

	iterateur_mention_courante = 0 # va donner l'indice de la mention courante dans le tableau des appreciations
	listeElevesPlaces = []

	while iterateur_mention_courante < 5 and liste_eleves_restants != [] :

		mentionCourante = liste_appreciations[iterateur_mention_courante] #Correspond à la mention minimale demandée pour qu un projet puisse etre attribué à un eleve

		#Boucle sur les projets (de 0 à 17 soit 18 projets)
		for k in range(nbre_projets):

			print "on s'interesse au ", k, "eme projet\n"

			#On crée la liste des eleves interessés par le projet k, ayant au moins mis la mention mentionCourante au projet considéré
			listeInteresses = creerListeEleveInteresses(liste_eleves_restants, k, mentionCourante)

			print "la liste des eleves intéressés est \n", listeInteresses, "\n"

			binomesElevesTemporaires = [] #liste des binomes que l'on peut creer à ce moment de l'algo pour le projet considéré

			#S'il y a au moins deux eleves dans cette liste, on pourra les comparer (pour eventuellement former un binome)
			if listeInteresses > 1:

				#On boucle sur les eleves de cette liste (à noter : on s'arrete à len-2 car le dernier eleve aura deja ete comparé avec tous les autres)
				for i in range(len(listeInteresses) - 2) :

					#On le compare aux autres eleves de cette liste et on ajoute les binomes d'eleves qui s apprecient
					for j in range(i+1, len(listeInteresses) - 1) :

						if elevesAcceptesEntreEux(listeInteresses[i], listeInteresses[j], liste_appreciations[iterateur_mention_courante + 1]):
							#On choisit ici iterateur mention courante + 1 car on veut privilegier de bonnes attributions de projets a de bonnes attributions de groupes d eleves

							binomesElevesTemporaires.append([listeInteresses[i], listeInteresses[j]])

						print "bin temp = ", binomesElevesTemporaires, "\n"

			print "-----------------------------------\n"
		iterateur_mention_courante += 1

main()
