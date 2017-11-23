# -*- coding: ISO-8859-1 -*-

import random;

#nbre_eleves = input("Entrer le nombre d'élèves de la promo (compris entre 36 et 54 élèves): ");
#while nbre_eleves < 36 or nbre_eleves > 54 :
#    nbre_eleves = input("Entrer une valeur à nouveau, le nombre d'élèves doit être compris entre 36 et 54 : ");

nbre_eleves = 10;
nbre_projets = 18;
nbre_trinomes = nbre_eleves - 36;
nbre_binomes = nbre_projets - nbre_trinomes;
print "Nbre de binome : %i  \nNbre de trinome : %i\n" % (nbre_binomes, nbre_trinomes)

liste_eleves_restants = [i for i in range(nbre_eleves)]
liste_appreciations_dispo = ["TB", "B", "AB", "P", "I", "AR"];
liste_appreciations_entre_eleves = [[random.choice(liste_appreciations_dispo) for j in range(nbre_eleves)] for i in range(nbre_eleves)];
print "Tableau des appreciations :\n", liste_appreciations_entre_eleves, "\n"
liste_groupes = []
ite_appreciation_courante = 0;

# on s'arrête lorqu'on a parcouru toutes les mentions ou qu'il n'y a plus d'élève à placer.
while ite_appreciation_courante < len(liste_appreciations_dispo) and ((not liste_eleves_restants) == False): #vérifie que la liste n'est pas vide

    appreciation_courante = liste_appreciations_dispo[ite_appreciation_courante]
    print appreciation_courante

    # parcours du tableau des appréciations avec appréciation_courante
    for i in range(nbre_eleves):

        # on regarde les apprec de l'élèves i que s'il n'est pas encore dans un groupe
        if i in liste_eleves_restants:

            print "-- new eleve %i\n" % i
            j = i+1

            # on s'arrête lorsqu'on a parcouru toutes les apprec de i ou lorsque i a été placé dans un groupe.
            while j < nbre_eleves and (i in liste_eleves_restants):

                apprec_ij = liste_appreciations_entre_eleves[i][j]
                print "new compa %i\n" % j

                # on regarde les apprec de l'élèves i sur j que si j n'est pas encore dans un groupe
                if j in liste_eleves_restants:

                    # si l'aprréciation de l'élève i sur j est aussi bien ou mieux que l'appréciation courante
                    if liste_appreciations_dispo.index(apprec_ij) <= ite_appreciation_courante:
                        apprec_ji = liste_appreciations_entre_eleves[j][i]

                        # si l'aprréciation de l'élève j sur i est aussi bien ou mieux que l'appréciation courante
                        if liste_appreciations_dispo.index(apprec_ji) <= ite_appreciation_courante:
                            liste_groupes.append([i,j])
                            print "élève à supprimer : %i, %i" % (i,j)
                            liste_eleves_restants.remove(i)
                            liste_eleves_restants.remove(j)

                j += 1
    ite_appreciation_courante += 1

print "Les groupes :\n", liste_groupes
print "élèves restants:\n", liste_eleves_restants
print (2 in liste_groupes)
