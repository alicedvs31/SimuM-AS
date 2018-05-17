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
# Prend en parametre lambda
def loiExpoTheorique(lambd, nb):
    resExpoTheo = []
    i = 0
    for i in range(nb):
        resExpoTheo.append(rand.expovariate(lambd))
    return resExpoTheo

def processPoi(tabEx):
    tabCum = []
    tabCum.append(tabEx[0])
    for i in range(1,len(tabEx)):
        tabCum.append(tabCum[i-1]+tabEx[i])
    return tabCum

def classeExp(tab):
    maxi = 0
    dernier = len(tab) - 1
    maxiTabExp = tab[dernier]
    print(maxiTabExp)

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
    print(len(tabExp))
    for i in range(len(tabExp)):
        tabExp.append(tabExp[i]-0.0001)
        tabExp.append(tabExp[i]+0.0001)
    tabExp.sort()
    return tabExp

# Classe permettant d'appeler l'interface
class ApplicationViewer(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = interSimu.Ui_MainWindow()
        self.ui.setupUi(self)



        # un clic sur le bouton appellera la méthode 'action_bouton'
        self.ui.validPara.clicked.connect(self.action_bouton)

    def action_bouton(self):
        NB_SIM = int(self.ui.nbEvt.toPlainText())
        print("NB_SIM  " + str(NB_SIM))
        LAM_DA = float(self.ui.varLambdArr.toPlainText())
        print("LAM_DA  " + str(LAM_DA))
        LAM_TRT = float(self.ui.varLambdTrt.toPlainText())
        print("LAM_TRT  " + str(LAM_TRT))

        env = self.ui.evtMark.isTristate()
        if (env == True):
            print("NON Markov")
        else:
            print("Markov")

        print("tableau nombres aleatoires")
        tabAlea = gene_rand(NB_SIM)
        print(tabAlea)
        print(len(tabAlea))

        #Process d'arrivee
        print("______________")
        print("loi exponentielle Arrivee")
        tabExpArr = loiExpo(tabAlea, LAM_DA)
        print(tabExpArr)

        print("______________")
        print("tableau processus poisson Arrivee")
        tabPoissArr = processPoi(tabExpArr)
        print(tabPoissArr)

        # Formatage des valeurs de la loi pour affichage
        list1 = tabAffichageExpo(tabPoissArr)

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
        list2 = tabAffichageExpo(tabPoissTrt)


        #Préparation graph processus de poissons
        y = tabRaie(NB_SIM)

        #x1 = []
        #x2 = []
        #for i in range(0,60):
        #    x1.append(tabAff1[i])
        #    x2.append(tabAff2[i])
        #print "x1"
        #print x1
        #print len(x1)
        #print "x2"


        #Graph arrivee
        self.ui.graphArrivee.axes.plot(list1,y)
        self.ui.graphArrivee.axes.set_xlim([0, 200])
        self.ui.graphArrivee.draw()

        #Graph traitement

        self.ui.graphTrait.axes.plot(list2,y)
        self.ui.graphTrait.axes.set_xlim([0, 200])
        self.ui.graphTrait.draw()


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
