# -*- coding: ISO-8859-1 -*-

import random;
import numpy as np;

#Constantes de l'algo
nbre_eleves = 44
nbre_projets = 17
nbre_trinomes = nbre_eleves - nbre_projets*2
nbre_binomes = nbre_projets - nbre_trinomes
print "Nbre de binomes : %i  \nNbre de trinomes : %i\n" % (nbre_binomes, nbre_trinomes)

liste_eleves_restants = [i for i in range(nbre_eleves)]
liste_appreciations = ["TB", "B", "AB", "P", "I", "AR"]

matrice_pref = np.array([[random.choice(liste_appreciations) for j in range(nbre_eleves)] for i in range(nbre_eleves)])
matrice_proj = np.array([[random.choice(liste_appreciations) for p in range(nbre_projets)] for i in range(nbre_eleves)])
print "Tableau des appreciations �l�ves :\n", matrice_pref, "\n"
print "Tableau des appreciations projets :\n", matrice_proj, "\n"

def creerListeDesMentionsAcceptables(m):
	# permet de creer la liste de toutes les mentions sup�rieures ou �gales � m

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
	# donn�es : i = i �me �l�ve, j = j �me �l�ve, m = mention minimale qu'il faut avoir entre les deux �l�ves
	# r�sultat : bool�en; vrai si les �l�ves se sont mis mutuellement au moins la mention m, faux sinon

	resultat = False
	mentions_accept = creerListeDesMentionsAcceptables(m)

	if ((matrice_pref[i][j] in mentions_accept) and (matrice_pref[j][i] in mentions_accept)):

		resultat = True

	return resultat


# def elevesAcceptentMemeProjet(i, j, p, m):
# 	# donn�es : i = i �me �l�ve, j = j �me �l�ve, p = num�ro du projet auquel on s'int�resse,
# 	# m = mention minimale qu'il faut avoir de la part de chacun des �l�ves pour le projet p
# 	# r�sultat : bool�en; vrai si les deux �l�ves ont au moins mis la mention m au projet p
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
	# donn�es : i = i �me �l�ve, p = numero du projet, m = mention mini que i doit avoir donn�e pour p
	# r�sultat : bool�en; vrai si i a au moins mis la mention m � p, faux sinon

	resultat = False
	mentions_accept = creerListeDesMentionsAcceptables(m)

	if (matrice_proj[i][p] in mentions_accept):

		resultat = True

	return resultat

def creerListeEleveInteresses(eleveRest, p, m):
	# donn�es : eleveRest : liste des eleves qu'il reste � placer; p : numero du projet auquel on s interesse; m : mention minimale voulue, attribu�e au projet p
	# resultat : liste des �l�ves (parmi les eleves qu il reste � placer) qui ont mis au moins la mention m � p

	resultat = []

	for i in eleveRest:

		if eleveAccepteProjet(i, p, m):

			resultat.append(i)

	return resultat


def creerBinomes(listeEleves, m):
	# donn�es : listeEl�ves : notre liste d �l�ve � comparer; m : mention minimale.
	# resultat : une liste de binomes, vide s'il n'y a pas de binomes possible.

	# i : it�rateur, l'�l�ve � partir duquel on construit la liste de ses binomes.
	# j : it�rateur qui parcourt la liste des �l�ves pour former un binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []

	i = 0;
	while listeLocaleEleves :
	# on boucle tant qu'il reste des �l�ves

		print "liste des �l�ves : ", listeLocaleEleves
		j = i + 1;
		binomeTrouve = False

		while j < len(listeLocaleEleves) and not binomeTrouve  :
		# parcours de la liste des �l�ves pour former binome
			 print "on compare ", listeLocaleEleves[i], " avec ", listeLocaleEleves[j]
			 if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				 resultat.append([listeLocaleEleves[i], listeLocaleEleves[j]])
				 print "un binome trouv� : ", resultat
				 listeLocaleEleves.remove(listeLocaleEleves[i])
				 listeLocaleEleves.remove(listeLocaleEleves[j-1])
				 binomeTrouve = True
			 j += 1

		if not binomeTrouve:
			print "on suppr ", listeLocaleEleves[i]
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "-----------------------------------\n"

	print "binome form�s : ", resultat
	return resultat

def creerBinome(listeEleves, m):
	# donn�es : listeEl�ves : notre liste d �l�ve � comparer; m : mention minimale.
	# resultat : le 1er binome trouv�, vide s'il n'y a pas de binomes possible.

	# i : it�rateur, l'�l�ve � partir duquel on construit la liste de ses binomes.
	# j : it�rateur qui parcourt la liste des �l�ves pour former un binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []
	binomeTrouve = False

	i = 0;
	while listeLocaleEleves and not binomeTrouve:
	# on boucle tant qu'il reste des �l�ves

		print "liste des �l�ves : ", listeLocaleEleves
		j = i + 1;

		while j < len(listeLocaleEleves) and not binomeTrouve  :
		# parcours de la liste des �l�ves pour former binome
			 print "on compare ", listeLocaleEleves[i], " avec ", listeLocaleEleves[j]
			 if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				 resultat = [listeLocaleEleves[i], listeLocaleEleves[j]]
				 print "un binome trouv� : ", resultat
				 listeLocaleEleves.remove(listeLocaleEleves[i])
				 listeLocaleEleves.remove(listeLocaleEleves[j-1])
				 binomeTrouve = True
			 j += 1

		if not binomeTrouve:
			print "on suppr ", listeLocaleEleves[i]
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "-----------------------------------\n"

	print "binome form� : ", resultat
	return resultat


def creerTrinomes(listeEleves, m, nb_trinomes):
	# donn�es : listeEl�ves : notre liste d �l�ve � comparer; m : mention minimale; nb_trinomes : le nombre de trinome que l'on peut former.
	# resultat : une liste de trinome, vide s'il n'y a pas de trinome possible.

	# i : it�rateur, l'�l�ve � partir duquel on construit la liste de ses binomes.
	# j : it�rateur qui parcourt la liste des �l�ves pour former un binome avec i.
	# k : it�rateur qui parcourt les binomes trouv�s de i.
	# l : it�rateur qui parcourt la liste des �l�ves pour former un trinome avec i et k.
	# listeBinomeAvecI : la liste des �l�ves pouvant �tre en binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []

	i = 0;
	while listeLocaleEleves and nb_trinomes > 0 :
	# on boucle tant qu'il reste des trinome � former

		print "liste des �l�ves : ", listeLocaleEleves
		j = i + 1;
		listeBinomeAvecI = []
		for j in range(i+1, len(listeLocaleEleves) - 1) :
		# on construit tous les binomes possibles avec l'�l�ve i.

			if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				listeBinomeAvecI.append(listeLocaleEleves[j])

		print "liste des binomes de ", listeLocaleEleves[i], " : ", listeBinomeAvecI
		trinomeTrouve = False

		if listeBinomeAvecI and len(listeBinomeAvecI) > 1:
		# si on a trouv� des binomes avec i, on essaye de construire des trinomes.
		# le 3eme �l�ve potentiel fera forc�ment parti des binomes possibles avec i.
			k = 0
			trinomeTrouve = False
			while k < len(listeBinomeAvecI) and not trinomeTrouve  :
			# parcours de chaque binome de i.

				l = k + 1
				trinomeTrouve = False

				while l < len(listeBinomeAvecI) and not trinomeTrouve  :
				# parcours de la liste des �l�ves pour former trinome.

					 print "on compare ", listeBinomeAvecI[k], " avec ", listeBinomeAvecI[l]
					 if elevesAcceptesEntreEux(listeBinomeAvecI[k], listeBinomeAvecI[l], m):

						 resultat.append([listeLocaleEleves[i], listeBinomeAvecI[k], listeBinomeAvecI[l]])
						 print "un trinome trouv� : ", resultat
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
		print "-----------------------------------\n"

	print "trinomes form�s : ", resultat
	return resultat

def creerTrinome(listeEleves, m):
	# donn�es : listeEl�ves : notre liste d �l�ve � comparer; m : mention minimale;
	# resultat : le premier trinome trouv�, vide s'il n'y a pas de trinome possible.

	# i : it�rateur, l'�l�ve � partir duquel on construit la liste de ses binomes.
	# j : it�rateur qui parcourt la liste des �l�ves pour former un binome avec i.
	# k : it�rateur qui parcourt les binomes trouv�s de i.
	# l : it�rateur qui parcourt la liste des �l�ves pour former un trinome avec i et k.
	# listeBinomeAvecI : la liste des �l�ves pouvant �tre en binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []
	trinomeTrouve = False

	i = 0;
	while listeLocaleEleves and not trinomeTrouve:
	# on boucle tant qu'il reste des trinome � former

		print "liste des �l�ves : ", listeLocaleEleves
		j = i + 1;
		listeBinomeAvecI = []
		for j in range(i+1, len(listeLocaleEleves) - 1) :
		# on construit tous les binomes possibles avec l'�l�ve i.

			if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				listeBinomeAvecI.append(listeLocaleEleves[j])

		print "liste des binomes de ", listeLocaleEleves[i], " : ", listeBinomeAvecI
		trinomeTrouve = False

		if listeBinomeAvecI and len(listeBinomeAvecI) > 1:
		# si on a trouv� des binomes avec i, on essaye de construire des trinomes.
		# le 3eme �l�ve potentiel fera forc�ment parti des binomes possibles avec i.
			k = 0
			while k < len(listeBinomeAvecI) and not trinomeTrouve  :
			# parcours de chaque binome de i.

				l = k + 1
				trinomeTrouve = False

				while l < len(listeBinomeAvecI) and not trinomeTrouve  :
				# parcours de la liste des �l�ves pour former trinome.

					 print "on compare ", listeBinomeAvecI[k], " avec ", listeBinomeAvecI[l]
					 if elevesAcceptesEntreEux(listeBinomeAvecI[k], listeBinomeAvecI[l], m):

						 resultat = [listeLocaleEleves[i], listeBinomeAvecI[k], listeBinomeAvecI[l]]
						 print "un trinome trouv� : ", resultat
						 listeLocaleEleves.remove(listeLocaleEleves[i])
						 listeLocaleEleves.remove(listeBinomeAvecI[k])
						 listeLocaleEleves.remove(listeBinomeAvecI[l])
						 trinomeTrouve = True
					 l += 1
				k += 1

		if not trinomeTrouve:
			print "on suppr"
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "-----------------------------------\n"

	print "trinome form� : ", resultat
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
	global nbre_eleves
	global nbre_projets
	global nbre_trinomes
	global nbre_binomes

	iterateur_mention_courante = 0 # va donner l'indice de la mention courante dans le tableau des appreciations
	listeElevesPlaces = []
	listeGroupes = []
	listeProjetsRestants = [i for i in range(nbre_projets)]

	while iterateur_mention_courante < 5 and liste_eleves_restants != [] :
		print "liste des �l�ves restants : ", liste_eleves_restants
		mentionCourante = liste_appreciations[iterateur_mention_courante] #Correspond � la mention minimale demand�e pour qu un projet puisse etre attribu� � un eleve

		#Boucle sur les projets (de 0 � 17 soit 18 projets)
		for k in range(len(listeProjetsRestants)):

			groupeTrouve = False

			print "on s'interesse au ", k, "eme projet\n"

			#On cr�e la liste des eleves interess�s par le projet k, ayant au moins mis la mention mentionCourante au projet consid�r�
			listeInteresses = creerListeEleveInteresses(liste_eleves_restants, k, mentionCourante)

			print "la liste des eleves int�ress�s pour trinomes est \n", listeInteresses, "\n"
			# listeGroupes = [] #liste des binomes que l'on peut creer � ce moment de l'algo pour le projet consid�r�

			#S'il y a au moins deux eleves dans cette liste, on pourra les comparer (pour eventuellement former un binome)
			if nbre_trinomes > 0 and len(listeInteresses) > 2 :
				# on r�cup�re les trinomes possibles
				trinomeForme = creerTrinome(listeInteresses, liste_appreciations[iterateur_mention_courante + 1])
				print "la liste restantes ", listeInteresses, "\n"
				
				# si on a trouv� un trinome 
				if trinomeForme :

					# on les ajoute � la liste des groupes
					listeGroupes.append	(trinomeForme)

					# on d�cr�mente le nombre de trinome
					nbre_trinomes -= 1

					# on  el�ve le projet que l'on vient de traiter
					del listeProjetsRestants[k]

					# on les supprime de nos �l�ves restants et de la liste des �l�ves int�ress�
					for eleve in trinomeForme:
						liste_eleves_restants.remove(eleve)
						listeInteresses.remove(eleve)
					groupeTrouve = True

			# s'il reste au moins 2 �l�ves int�ress�
			print "la liste des eleves int�ress�s pour binomes est \n", listeInteresses, "\n"

			if not groupeTrouve and len(listeInteresses) > 1 :
				# on r�cup�re les binomes possibles
				binomeForme = creerBinome(listeInteresses, liste_appreciations[iterateur_mention_courante + 1])

	
				if binomeForme :

					# on les ajoute � la liste des groupes
					listeGroupes.append(binomeForme)

					# on  el�ve le projet que l'on vient de traiter
					del listeProjetsRestants[k]

						# on les supprime de nos �l�ves restants et de la liste des �l�ves int�ress�
						for eleve in binomeForme:
							print "eleve a suppr : ", eleve
							liste_eleves_restants.remove(eleve)
							listeInteresses.remove(eleve)

			# 	#On boucle sur les eleves de cette liste (� noter : on s'arrete � len-2 car le dernier eleve aura deja ete compar� avec tous les autres)
			# 	for i in range(len(listeInteresses) - 2) :
			#
			# 		#On le compare aux autres eleves de cette liste et on ajoute les binomes d'eleves qui s apprecient
			# 		for j in range(i+1, len(listeInteresses) - 1) :
			#
			# 			if elevesAcceptesEntreEux(listeInteresses[i], listeInteresses[j], liste_appreciations[iterateur_mention_courante + 1]):
			# 				#On choisit ici iterateur mention courante + 1 car on veut privilegier de bonnes attributions de projets a de bonnes attributions de groupes d eleves
			#
			# 				binomesElevesTemporaires.append([listeInteresses[i], listeInteresses[j]])
			#
			# 			print "bin temp = ", binomesElevesTemporaires, "\n"
			print "liste Groupes : ", listeGroupes

			print "-----------------------------------\n"
		iterateur_mention_courante += 1

main()
# creerBinome(liste_eleves_restants, "P")
