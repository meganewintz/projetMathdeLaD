# -*- coding: ISO-8859-1 -*-

import random;
import numpy as np;

#Constantes de l'algo
nbre_eleves = 44
nbre_projets = 18
nbre_trinomes = nbre_eleves - nbre_projets*2
nbre_binomes = nbre_projets - nbre_trinomes
print "Nbre de binomes : %i  \nNbre de trinomes : %i\n" % (nbre_binomes, nbre_trinomes)

liste_eleves_restants = [i for i in range(nbre_eleves)]
liste_appreciations = ["TB", "B", "AB", "P", "I", "AR"]

matrice_pref = np.array([[random.choice(liste_appreciations) for j in range(nbre_eleves)] for i in range(nbre_eleves)])
matrice_proj = np.array([[random.choice(liste_appreciations) for p in range(nbre_projets)] for i in range(nbre_eleves)])
print "Tableau des appreciations eleves :\n", matrice_pref, "\n"
print "Tableau des appreciations projets :\n", matrice_proj, "\n"

def creerListeDesMentionsAcceptables(m):
	# permet de creer la liste de toutes les mentions superieures ou egales e m

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
	# donnees : i = i eme eleve, j = j eme eleve, m = mention minimale qu'il faut avoir entre les deux eleves
	# resultat : booleen; vrai si les eleves se sont mis mutuellement au moins la mention m, faux sinon

	resultat = False
	mentions_accept = creerListeDesMentionsAcceptables(m)

	if ((matrice_pref[i][j] in mentions_accept) and (matrice_pref[j][i] in mentions_accept)):

		resultat = True

	return resultat


# def elevesAcceptentMemeProjet(i, j, p, m):
# 	# donnees : i = i eme eleve, j = j eme eleve, p = numero du projet auquel on s'interesse,
# 	# m = mention minimale qu'il faut avoir de la part de chacun des eleves pour le projet p
# 	# resultat : booleen; vrai si les deux eleves ont au moins mis la mention m au projet p
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
	# donnees : i = i eme eleve, p = numero du projet, m = mention mini que i doit avoir donnee pour p
	# resultat : booleen; vrai si i a au moins mis la mention m e p, faux sinon

	resultat = False
	mentions_accept = creerListeDesMentionsAcceptables(m)

	if (matrice_proj[i][p] in mentions_accept):

		resultat = True

	return resultat

def creerListeEleveInteresses(eleveRest, p, m):
	# donnees : eleveRest : liste des eleves qu'il reste e placer; p : numero du projet auquel on s interesse; m : mention minimale voulue, attribuee au projet p
	# resultat : liste des eleves (parmi les eleves qu il reste e placer) qui ont mis au moins la mention m e p

	resultat = []

	for i in eleveRest:

		if eleveAccepteProjet(i, p, m):

			resultat.append(i)

	return resultat


def creerBinomes(listeEleves, m):
	# donnees : listeEleves : notre liste d eleve e comparer; m : mention minimale.
	# resultat : une liste de binomes, vide s'il n'y a pas de binomes possible.

	# i : iterateur, l'eleve e partir duquel on construit la liste de ses binomes.
	# j : iterateur qui parcourt la liste des eleves pour former un binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []

	i = 0;
	while listeLocaleEleves :
	# on boucle tant qu'il reste des eleves

		print "liste des eleves : ", listeLocaleEleves
		j = i + 1;
		binomeTrouve = False

		while j < len(listeLocaleEleves) and not binomeTrouve  :
		# parcours de la liste des eleves pour former binome
			 print "on compare ", listeLocaleEleves[i], " avec ", listeLocaleEleves[j]
			 if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				 resultat.append([listeLocaleEleves[i], listeLocaleEleves[j]])
				 print "un binome trouve : ", resultat
				 listeLocaleEleves.remove(listeLocaleEleves[i])
				 listeLocaleEleves.remove(listeLocaleEleves[j-1])
				 binomeTrouve = True
			 j += 1

		if not binomeTrouve:
			print "on suppr ", listeLocaleEleves[i]
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "\n"

	print "binome formes : ", resultat
	return resultat

def creerBinome(listeEleves, m):
	# donnees : listeEleves : notre liste d eleve e comparer; m : mention minimale.
	# resultat : le 1er binome trouve, vide s'il n'y a pas de binomes possible.

	# i : iterateur, l'eleve e partir duquel on construit la liste de ses binomes.
	# j : iterateur qui parcourt la liste des eleves pour former un binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []
	binomeTrouve = False

	print "Construction des binomes : \n"

	i = 0;
	while listeLocaleEleves and not binomeTrouve:
	# on boucle tant qu'il reste des eleves

		print "liste des eleves : ", listeLocaleEleves
		j = i + 1;

		while j < len(listeLocaleEleves) and not binomeTrouve  :
		# parcours de la liste des eleves pour former binome
			 print "on compare ", listeLocaleEleves[i], " avec ", listeLocaleEleves[j]
			 if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				 resultat = [listeLocaleEleves[i], listeLocaleEleves[j]]
				 print "un binome trouve : ", resultat
				 listeLocaleEleves.remove(listeLocaleEleves[i])
				 listeLocaleEleves.remove(listeLocaleEleves[j-1])
				 binomeTrouve = True
			 j += 1

		if not binomeTrouve:
			print "on suppr ", listeLocaleEleves[i]
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "\n"

	print "binome forme : ", resultat
	return resultat


def creerTrinomes(listeEleves, m, nb_trinomes):
	# donnees : listeEleves : notre liste d eleve e comparer; m : mention minimale; nb_trinomes : le nombre de trinome que l'on peut former.
	# resultat : une liste de trinome, vide s'il n'y a pas de trinome possible.

	# i : iterateur, l'eleve e partir duquel on construit la liste de ses binomes.
	# j : iterateur qui parcourt la liste des eleves pour former un binome avec i.
	# k : iterateur qui parcourt les binomes trouves de i.
	# l : iterateur qui parcourt la liste des eleves pour former un trinome avec i et k.
	# listeBinomeAvecI : la liste des eleves pouvant etre en binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []

	i = 0;
	while listeLocaleEleves and nb_trinomes > 0 :
	# on boucle tant qu'il reste des trinome e former

		print "liste des eleves : ", listeLocaleEleves
		j = i + 1;
		listeBinomeAvecI = []
		for j in range(i+1, len(listeLocaleEleves)) :
		# on construit tous les binomes possibles avec l'eleve i.

			if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				listeBinomeAvecI.append(listeLocaleEleves[j])

		print "liste des binomes de ", listeLocaleEleves[i], " : ", listeBinomeAvecI
		trinomeTrouve = False

		if listeBinomeAvecI and len(listeBinomeAvecI) > 1:
		# si on a trouve des binomes avec i, on essaye de construire des trinomes.
		# le 3eme eleve potentiel fera forcement parti des binomes possibles avec i.
			k = 0
			trinomeTrouve = False
			while k < len(listeBinomeAvecI) and not trinomeTrouve  :
			# parcours de chaque binome de i.

				l = k + 1
				trinomeTrouve = False

				while l < len(listeBinomeAvecI) and not trinomeTrouve  :
				# parcours de la liste des eleves pour former trinome.

					 print "on compare ", listeBinomeAvecI[k], " avec ", listeBinomeAvecI[l]
					 if elevesAcceptesEntreEux(listeBinomeAvecI[k], listeBinomeAvecI[l], m):

						 resultat.append([listeLocaleEleves[i], listeBinomeAvecI[k], listeBinomeAvecI[l]])
						 print "un trinome trouve : ", resultat
						 listeLocaleEleves.remove(listeLocaleEleves[i])
						 listeLocaleEleves.remove(listeBinomeAvecI[k])
						 listeLocaleEleves.remove(listeBinomeAvecI[l])
						 trinomeTrouve = True
						 nb_trinomes -= 1
					 l += 1
				k += 1

		if not trinomeTrouve:
			print "on suppr"
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "\n"

	print "trinomes formes : ", resultat
	return resultat

def creerTrinome(listeEleves, m):
	# donnees : listeEleves : notre liste d eleve e comparer; m : mention minimale;
	# resultat : le premier trinome trouve, vide s'il n'y a pas de trinome possible.

	# i : iterateur, l'eleve e partir duquel on construit la liste de ses binomes.
	# j : iterateur qui parcourt la liste des eleves pour former un binome avec i.
	# k : iterateur qui parcourt les binomes trouves de i.
	# l : iterateur qui parcourt la liste des eleves pour former un trinome avec i et k.
	# listeBinomeAvecI : la liste des eleves pouvant etre en binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []
	trinomeTrouve = False

	print "Construction des trinomes : \n"

	i = 0;
	while listeLocaleEleves and not trinomeTrouve:
	# on boucle tant qu'il reste des trinome e former

		print "liste des eleves : ", listeLocaleEleves
		j = i + 1;
		listeBinomeAvecI = []
		for j in range(i+1, len(listeLocaleEleves)) :
		# on construit tous les binomes possibles avec l'eleve i.

			if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				listeBinomeAvecI.append(listeLocaleEleves[j])

		print "liste des binomes de ", listeLocaleEleves[i], " : ", listeBinomeAvecI
		trinomeTrouve = False

		if listeBinomeAvecI and len(listeBinomeAvecI) > 1:
		# si on a trouve des binomes avec i, on essaye de construire des trinomes.
		# le 3eme eleve potentiel fera forcement parti des binomes possibles avec i.
			k = 0
			while k < len(listeBinomeAvecI) and not trinomeTrouve  :
			# parcours de chaque binome de i.

				l = k + 1
				trinomeTrouve = False

				while l < len(listeBinomeAvecI) and not trinomeTrouve  :
				# parcours de la liste des eleves pour former trinome.

					 print "on compare ", listeBinomeAvecI[k], " avec ", listeBinomeAvecI[l]
					 if elevesAcceptesEntreEux(listeBinomeAvecI[k], listeBinomeAvecI[l], m):

						 resultat = [listeLocaleEleves[i], listeBinomeAvecI[k], listeBinomeAvecI[l]]
						 print "un trinome trouve : ", resultat
						 listeLocaleEleves.remove(listeLocaleEleves[i])
						 listeLocaleEleves.remove(listeBinomeAvecI[k])
						 listeLocaleEleves.remove(listeBinomeAvecI[l])
						 trinomeTrouve = True
					 l += 1
				k += 1

		if not trinomeTrouve:
			print "on suppr"
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "\n"

	print "trinome forme : ", resultat
	return resultat

'''
#######################################################
#######################################################
#######################################################
#######################################################
'''

def main():
	global nbre_eleves
	global nbre_projets
	global nbre_trinomes
	global nbre_binomes

	iterateur_mention_courante = 0 # va donner l'indice de la mention courante dans le tableau des appreciations
	listeElevesPlaces = []
	listeGroupes = []
	listeProjetsRestants = [i for i in range(nbre_projets)]

	print "nombre de trinome à former : ", nbre_trinomes
	while iterateur_mention_courante < len(liste_appreciations) and liste_eleves_restants != [] :

		# Correspond a la mention minimale demandee pour qu un projet puisse etre attribue a un eleve
		mentionCourante = liste_appreciations[iterateur_mention_courante]

		print "\n--------------------------------------------\n"
		print "Mention courante : ", mentionCourante
		print "\n--------------------------------------------\n"


		#Boucle sur les projets dispo
		k = 0
		while k < len(listeProjetsRestants):
				groupeTrouve = False

				print "on s'interesse au ", listeProjetsRestants[k], "eme projet, avec mention", liste_appreciations[iterateur_mention_courante], "\n"
				print "liste des eleves restants : ", liste_eleves_restants
				print "liste des projets restants ", listeProjetsRestants

				#On cree la liste des eleves interesses par le projet k, ayant au moins mis la mention mentionCourante au projet considere
				listeInteresses = creerListeEleveInteresses(liste_eleves_restants, listeProjetsRestants[k], mentionCourante)

				print "la liste des eleves interesses pour trinomes est \n", listeInteresses, "\n"

				#S'il y a au moins deux eleves dans cette liste, on pourra les comparer (pour eventuellement former un binome)
				if nbre_trinomes > 0 and len(listeInteresses) > 2 :

					# on recupere les trinomes possibles
					trinomeForme = creerTrinome(listeInteresses, liste_appreciations[iterateur_mention_courante])

					print "la liste restantes ", listeInteresses, "\n"

					# si on a trouve un trinome
					if trinomeForme :

						# on les ajoute a la liste des groupes
						listeGroupes.append([listeProjetsRestants[k], trinomeForme, mentionCourante])

						# on decremente le nombre de trinome
						nbre_trinomes -= 1

						# on  eleve le projet que l'on vient de traiter
						listeProjetsRestants.remove(listeProjetsRestants[k])

						# on les supprime de nos eleves restants et de la liste des eleves interesse
						for eleve in trinomeForme:
							liste_eleves_restants.remove(eleve)
							listeInteresses.remove(eleve)
						groupeTrouve = True

				# s'il reste au moins 2 eleves interesse
				if not groupeTrouve and nbre_binomes > 0 and len(listeInteresses) > 1 :

					print "la liste des eleves interesses pour binomes est \n", listeInteresses, "\n"

					# on recupere les binomes possibles
					binomeForme = creerBinome(listeInteresses, liste_appreciations[iterateur_mention_courante])

					if binomeForme :

						# on les ajoute a la liste des groupes
						listeGroupes.append([listeProjetsRestants[k], binomeForme, mentionCourante])

						# on  eleve le projet que l'on vient de traiter
						listeProjetsRestants.remove(listeProjetsRestants[k])

						# on decremente le nombre de binome
						nbre_binomes -= 1

						# on les supprime de nos eleves restants et de la liste des eleves interesse
						for eleve in binomeForme:
							print "eleve a suppr : ", eleve
							liste_eleves_restants.remove(eleve)
							listeInteresses.remove(eleve)
						groupeTrouve = True

				# on incrémente k que si on n'a pas trouvé de groupe, car sinon on a supprimé le projet donc les indices se sont décallés.
				if not groupeTrouve:
					k += 1
				print "liste Groupes : ", listeGroupes
				print "liste des eleves restants : ", liste_eleves_restants
				print "liste des projets restants  :", listeProjetsRestants
				print "trinome restants à former : ", nbre_trinomes
				print "binome restants à former : ", nbre_binomes

				print "\n--------------------------------------------\n"
		iterateur_mention_courante += 1

main()
# creerBinome(liste_eleves_restants, "P")
