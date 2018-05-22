# coding=utf-8
# Importation des Librairies
from PyQt4.QtGui import *
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import interSimu
from interSimu import Ui_MainWindow


# Genere une liste de nombre aléatoire de taille NB_SIM en utilisant la fonction random de python
def gene_rand(nb):
    #Genere 100 nombres aleatoires a 4 decimales
    l = [round(rand.random(),4) for i in range(nb)]
    return l


# Genere une liste de nombre suivant une loi exponentielle prenant en paramètre une liste de nombre aléatoire et lambda
def loiExpo(tabAlea, lambd):
    res = [round((-math.log(i)/lambd),4) for i in tabAlea]
    return res


# Genere une liste suivant une loi exponentielle theorique en utilisant la fonction expovariate de la bibliotheque random
# Prend en parametre lambda, et le nombre de simulation
def loiExpoTheorique(lambd, nb):
    resExpoTheo = []
    i = 0
    for i in range(nb):
        resExpoTheo.append(rand.expovariate(lambd))
    return resExpoTheo


# Genere une liste de nombre aleatoires suivant une loi de poisson
#prend en parametre le tableau de valeurs aleatoires genere par la loi exponentielle
def processPoi(tabEx):
    tabCum = []
    tabCum.append(tabEx[0])
    for i in range(1,len(tabEx)):
        tabCum.append(tabCum[i-1]+tabEx[i])
    return tabCum


# Genere une liste suivant une loi normale à la valeur absolue pour pouvoir exploiter les valeurs
#prend en parametre deux listes de nombres alea de taille NB_SIM et lambda
def loiNormale(listeAlea1, listeAlea2, lambd):
    tabNorm = []
    s=1/lambd
    m=1/lambd
    for i in range(len(listeAlea1)):
        tabNorm.append(math.fabs(math.sqrt(-2*math.log(listeAlea1[i]))*math.cos(2*math.pi*listeAlea2[i]))*s+m)
    return tabNorm


# Renvoie un tableau contenant uniquement des 1 entouré de deux 0
# Cette liste permet ensuite de tracer le spectre de raie en montant à 1 pour chaque valeur de notre liste et restant à 0 le reste du temps
def tabRaie(nb):
    resRaie = []
    for i in range(nb):
        resRaie.append(0)
        resRaie.append(1)
        resRaie.append(0)
    return resRaie


# Permet de généré une liste utilisée pour la représentation graphique des raies d'une loi
# On entoure chaque valeur de notre liste avec une valeur très proche inférieur et supérieur qui prendront comme valeur 0
def tabAffichageExpo(tabExp):
    tabExp_Copy = tabExp[:]
    print(len(tabExp))
    for i in range(len(tabExp)):
        tabExp_Copy.append(tabExp[i]-0.0001)
        tabExp_Copy.append(tabExp[i]+0.0001)
    tabExp_Copy.sort()
    return tabExp_Copy


# Permet de transformer le tableau de poisson des traitement en tableau de duree
def tabToDuree(tab):
    tabDur =[]
    tabDur.append(tab[0])
    for i in range(1,len(tab)):
        tabDur.append(tab[i]-tab[i-1])
    return tabDur


# Permet de dire si une piece va etre mise en attente
# prend en parametre l'arrivee de la piece, sa duree de traitement et l'arrivee de la piece suivante
def stop_piece(piece, piece_suivante, tmp_fabricatio):
    intervalle = piece_suivante - piece
    if intervalle < tmp_fabricatio:
        return True
    else:
        return False



# Classe permettant d'appeler l'interface
class ApplicationViewer(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = interSimu.Ui_MainWindow()
        self.ui.setupUi(self)



        # un clic sur le bouton appellera la méthode 'action_bouton'
        self.ui.validPara.clicked.connect(self.action_bouton)

    def action_bouton(self):
        # Bloc recuperant les var de l'interface saisies par l'utilisateur
        NB_SIM = int(self.ui.nbEvt.toPlainText())
        print("NB_SIM  " + str(NB_SIM))
        LAM_DA = float(self.ui.varLambdArr.toPlainText())
        print("LAM_DA  " + str(LAM_DA))
        LAM_TRT = float(self.ui.varLambdTrt.toPlainText())
        print("LAM_TRT  " + str(LAM_TRT))

        # Generation des nombres aleatoires
        tabAlea = gene_rand(NB_SIM)

        # Si l'utilisateur a choisit d'etre en environnement markovien
        if self.ui.evtMark.isChecked() :
            print("Markov")
            #Process d'arrivee loi exponentielle
            print("______________")
            print("loi exponentielle Arrivee")
            tabExpArr = loiExpo(tabAlea, LAM_DA)
            print(tabExpArr)

            #Process d'arrivee loi de poisson
            print("______________")
            print("tableau processus poisson Arrivee")
            tabPoissArr = processPoi(tabExpArr)
            print(tabPoissArr)

            # Formatage des valeurs de la loi pour affichage
            x1 = tabAffichageExpo(tabPoissArr)

        # Sinon on est en processus non markovien
        else:
            #Process d'arrivee loi normale
            print("loi normale Arrivee")
            # Generation de deux tableau de valeurs aleatoires
            tabAlea1 = gene_rand(NB_SIM)
            tabAlea2 = gene_rand(NB_SIM)
            tabNormale = loiNormale(tabAlea1, tabAlea2, LAM_DA)
            print(tabNormale)

            #Process arrivee loi normale
            tabNormalePoi = processPoi(tabNormale)
            x1 = tabAffichageExpo(tabNormalePoi)



    ###############################################
    #Process traitement
        print("______________")
        print("loi exponentielle Traitement")
        tabExpTrt = loiExpo(tabAlea, LAM_TRT)
        print(tabExpTrt)

        print("______________")
        print("tableau processus poisson Traitement")
        tabPoissTrt = processPoi(tabExpTrt)
        print(tabPoissTrt)


        # Formatage des valeurs de la loi pour affichage
        x2 = tabAffichageExpo(tabPoissTrt)

        y = tabRaie(NB_SIM)

        #Graph arrivee
        self.ui.graphArrivee.axes.plot(x1,y)
        self.ui.graphArrivee.axes.set_xlim([0, 600])
        self.ui.graphArrivee.draw()

        #Graph traitement
        self.ui.graphTrait.axes.plot(x2,y)
        self.ui.graphTrait.axes.set_xlim([0, 600])
        self.ui.graphTrait.draw()


        ####################################
        #dernier graph



# Fonction main
if __name__=="__main__":
    # Appel de l'interface
    app = QApplication(sys.argv)
    applicationViewer = ApplicationViewer()
    applicationViewer.show()
    sys.exit(app.exec_())


    print("______________")
    print("loi exponentielle theorique")
    tabExpoTheorique = loiExpoTheorique(0.05)
    print(tabExpoTheorique)


    print("______________")
    print("tableau expo theorique trie")
    tabExpoTheorique.sort()
    print(tabExpoTheorique)

    # Traçage du graphique
    plt.plot(tabStyle, tabRaie)
    plt.show()
