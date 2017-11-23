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


def creerBinomes(listeEleves, m):
	# données : listeElèves : notre liste d élève à comparer; m : mention minimale.
	# resultat : une liste de binomes, vide s'il n'y a pas de binomes possible.

	# i : itérateur, l'élève à partir duquel on construit la liste de ses binomes.
	# j : itérateur qui parcourt la liste des élèves pour former un binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []

	i = 0;
	while listeLocaleEleves :
	# on boucle tant qu'il reste des élèves

		print "liste des élèves : ", listeLocaleEleves
		j = i + 1;
		binomeTrouve = False

		while j < len(listeLocaleEleves) and not binomeTrouve  :
		# parcours de la liste des élèves pour former binome
			 print "on compare ", listeLocaleEleves[i], " avec ", listeLocaleEleves[j]
			 if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				 resultat.append([listeLocaleEleves[i], listeLocaleEleves[j]])
				 print "un binome trouvé : ", resultat
				 listeLocaleEleves.remove(listeLocaleEleves[i])
				 listeLocaleEleves.remove(listeLocaleEleves[j-1])
				 binomeTrouve = True
			 j += 1

		if not binomeTrouve:
			print "on suppr ", listeLocaleEleves[i]
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "-----------------------------------\n"

	print "binome formés : ", resultat
	return resultat

def creerBinome(listeEleves, m):
	# données : listeElèves : notre liste d élève à comparer; m : mention minimale.
	# resultat : le 1er binome trouvé, vide s'il n'y a pas de binomes possible.

	# i : itérateur, l'élève à partir duquel on construit la liste de ses binomes.
	# j : itérateur qui parcourt la liste des élèves pour former un binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []
	binomeTrouve = False

	i = 0;
	while listeLocaleEleves and not binomeTrouve:
	# on boucle tant qu'il reste des élèves

		print "liste des élèves : ", listeLocaleEleves
		j = i + 1;

		while j < len(listeLocaleEleves) and not binomeTrouve  :
		# parcours de la liste des élèves pour former binome
			 print "on compare ", listeLocaleEleves[i], " avec ", listeLocaleEleves[j]
			 if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				 resultat = [listeLocaleEleves[i], listeLocaleEleves[j]]
				 print "un binome trouvé : ", resultat
				 listeLocaleEleves.remove(listeLocaleEleves[i])
				 listeLocaleEleves.remove(listeLocaleEleves[j-1])
				 binomeTrouve = True
			 j += 1

		if not binomeTrouve:
			print "on suppr ", listeLocaleEleves[i]
			listeLocaleEleves.remove(listeLocaleEleves[i])
		print "-----------------------------------\n"

	print "binome formé : ", resultat
	return resultat


def creerTrinomes(listeEleves, m, nb_trinomes):
	# données : listeElèves : notre liste d élève à comparer; m : mention minimale; nb_trinomes : le nombre de trinome que l'on peut former.
	# resultat : une liste de trinome, vide s'il n'y a pas de trinome possible.

	# i : itérateur, l'élève à partir duquel on construit la liste de ses binomes.
	# j : itérateur qui parcourt la liste des élèves pour former un binome avec i.
	# k : itérateur qui parcourt les binomes trouvés de i.
	# l : itérateur qui parcourt la liste des élèves pour former un trinome avec i et k.
	# listeBinomeAvecI : la liste des élèves pouvant être en binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []

	i = 0;
	while listeLocaleEleves and nb_trinomes > 0 :
	# on boucle tant qu'il reste des trinome à former

		print "liste des élèves : ", listeLocaleEleves
		j = i + 1;
		listeBinomeAvecI = []
		for j in range(i+1, len(listeLocaleEleves) - 1) :
		# on construit tous les binomes possibles avec l'élève i.

			if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				listeBinomeAvecI.append(listeLocaleEleves[j])

		print "liste des binomes de ", listeLocaleEleves[i], " : ", listeBinomeAvecI
		trinomeTrouve = False

		if listeBinomeAvecI and len(listeBinomeAvecI) > 1:
		# si on a trouvé des binomes avec i, on essaye de construire des trinomes.
		# le 3eme élève potentiel fera forcément parti des binomes possibles avec i.
			k = 0
			trinomeTrouve = False
			while k < len(listeBinomeAvecI) and not trinomeTrouve  :
			# parcours de chaque binome de i.

				l = k + 1
				trinomeTrouve = False

				while l < len(listeBinomeAvecI) and not trinomeTrouve  :
				# parcours de la liste des élèves pour former trinome.

					 print "on compare ", listeBinomeAvecI[k], " avec ", listeBinomeAvecI[l]
					 if elevesAcceptesEntreEux(listeBinomeAvecI[k], listeBinomeAvecI[l], m):

						 resultat.append([listeLocaleEleves[i], listeBinomeAvecI[k], listeBinomeAvecI[l]])
						 print "un trinome trouvé : ", resultat
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

	print "trinomes formés : ", resultat
	return resultat

def creerTrinome(listeEleves, m):
	# données : listeElèves : notre liste d élève à comparer; m : mention minimale;
	# resultat : le premier trinome trouvé, vide s'il n'y a pas de trinome possible.

	# i : itérateur, l'élève à partir duquel on construit la liste de ses binomes.
	# j : itérateur qui parcourt la liste des élèves pour former un binome avec i.
	# k : itérateur qui parcourt les binomes trouvés de i.
	# l : itérateur qui parcourt la liste des élèves pour former un trinome avec i et k.
	# listeBinomeAvecI : la liste des élèves pouvant être en binome avec i.

	listeLocaleEleves = listeEleves[:]
	resultat = []
	trinomeTrouve = False

	i = 0;
	while listeLocaleEleves and not trinomeTrouve:
	# on boucle tant qu'il reste des trinome à former

		print "liste des élèves : ", listeLocaleEleves
		j = i + 1;
		listeBinomeAvecI = []
		for j in range(i+1, len(listeLocaleEleves) - 1) :
		# on construit tous les binomes possibles avec l'élève i.

			if elevesAcceptesEntreEux(listeLocaleEleves[i], listeLocaleEleves[j], m):
				listeBinomeAvecI.append(listeLocaleEleves[j])

		print "liste des binomes de ", listeLocaleEleves[i], " : ", listeBinomeAvecI
		trinomeTrouve = False

		if listeBinomeAvecI and len(listeBinomeAvecI) > 1:
		# si on a trouvé des binomes avec i, on essaye de construire des trinomes.
		# le 3eme élève potentiel fera forcément parti des binomes possibles avec i.
			k = 0
			while k < len(listeBinomeAvecI) and not trinomeTrouve  :
			# parcours de chaque binome de i.

				l = k + 1
				trinomeTrouve = False

				while l < len(listeBinomeAvecI) and not trinomeTrouve  :
				# parcours de la liste des élèves pour former trinome.

					 print "on compare ", listeBinomeAvecI[k], " avec ", listeBinomeAvecI[l]
					 if elevesAcceptesEntreEux(listeBinomeAvecI[k], listeBinomeAvecI[l], m):

						 resultat = [listeLocaleEleves[i], listeBinomeAvecI[k], listeBinomeAvecI[l]]
						 print "un trinome trouvé : ", resultat
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

	print "trinome formé : ", resultat
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
		print "liste des élèves restants : ", liste_eleves_restants
		mentionCourante = liste_appreciations[iterateur_mention_courante] #Correspond à la mention minimale demandée pour qu un projet puisse etre attribué à un eleve

		#Boucle sur les projets (de 0 à 17 soit 18 projets)
		for k in range(len(listeProjetsRestants)):

			groupeTrouve = False

			print "on s'interesse au ", k, "eme projet\n"

			#On crée la liste des eleves interessés par le projet k, ayant au moins mis la mention mentionCourante au projet considéré
			listeInteresses = creerListeEleveInteresses(liste_eleves_restants, k, mentionCourante)

			print "la liste des eleves intéressés pour trinomes est \n", listeInteresses, "\n"
			# listeGroupes = [] #liste des binomes que l'on peut creer à ce moment de l'algo pour le projet considéré

			#S'il y a au moins deux eleves dans cette liste, on pourra les comparer (pour eventuellement former un binome)
			if nbre_trinomes > 0 and len(listeInteresses) > 2 :
				# on récupère les trinomes possibles
				trinomeForme = creerTrinome(listeInteresses, liste_appreciations[iterateur_mention_courante + 1])
				print "la liste restantes ", listeInteresses, "\n"
				
				# si on a trouvé un trinome 
				if trinomeForme :

					# on les ajoute à la liste des groupes
					listeGroupes.append	(trinomeForme)

					# on décrémente le nombre de trinome
					nbre_trinomes -= 1

					# on  elève le projet que l'on vient de traiter
					del listeProjetsRestants[k]

					# on les supprime de nos élèves restants et de la liste des élèves intéressé
					for eleve in trinomeForme:
						liste_eleves_restants.remove(eleve)
						listeInteresses.remove(eleve)
					groupeTrouve = True

			# s'il reste au moins 2 élèves intéressé
			print "la liste des eleves intéressés pour binomes est \n", listeInteresses, "\n"

			if not groupeTrouve and len(listeInteresses) > 1 :
				# on récupère les binomes possibles
				binomeForme = creerBinome(listeInteresses, liste_appreciations[iterateur_mention_courante + 1])

	
				if binomeForme :

					# on les ajoute à la liste des groupes
					listeGroupes.append(binomeForme)

					# on  elève le projet que l'on vient de traiter
					del listeProjetsRestants[k]

						# on les supprime de nos élèves restants et de la liste des élèves intéressé
						for eleve in binomeForme:
							print "eleve a suppr : ", eleve
							liste_eleves_restants.remove(eleve)
							listeInteresses.remove(eleve)

			# 	#On boucle sur les eleves de cette liste (à noter : on s'arrete à len-2 car le dernier eleve aura deja ete comparé avec tous les autres)
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
