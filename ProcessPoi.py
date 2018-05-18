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

# Genere une liste suivant une loi normale à la valeur absolue pour pouvoir exploiter les valeurs
def loiNormale(listeAlea1, listeAlea2, lambd):
    tabNorm = []
    s=1/lambd
    m=1/lambd
    for i in range(len(listeAlea1)):
        tabNorm.append(math.fabs(math.sqrt(-2*math.log(listeAlea1[i]))*math.cos(2*math.pi*listeAlea2[i]))*s+m)
    return tabNorm

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

def chaineProdtest(tabA, tabB, nb):
    tabChaine = []
    tabChaine.append(tabA[0])
    tabChaine.append(tabA[0] + tabB[0])
    for i in range(2,nb-1) :
        tabChaine.append(tabA[i] + (tabB[i+1] - tabB[i]))
    return tabChaine

def attente(tabarr,valdeb, valfin,nb):
    cmpt = 0
    tabIndice = []
    for i in range(0,nb-1):
        if valdeb < tabarr[i] <valfin :
            cmpt = cmpt + 1
            tabIndice.append(i)
    return cmpt, tabIndice

def tabToDuree(tab):
    tabDur =[]
    tabDur.append(tab[0])
    for i in range(1,len(tab)):
        tabDur.append(tab[i]-tab[i-1])
    return tabDur

def chaineProd(tabA, tabB, nb):
    duree = tabToDuree(tabB)
    tabChaine = []
    xtimeAttente = [tabA[0]]
    ynbAttente = [0]
    tabChaine.append(tabA[0])
    if tabA[1]<duree[0]:
        xtimeAttente.append(tabA[1])
        ynbAttente.append(1)
        tabChaine.append(tabA[0] + duree[0])
    else:
        xtimeAttente.append(tabA[1])
        ynbAttente.append(0)
        tabChaine.append(tabA[1])

    iArr = 2
    iDur = 1
    cumulAtt = 0
    for i in range(2,nb-1):
        while iDur < nb-1:
            valAtt, queue = attente(tabA, tabChaine[i-1], tabChaine[i-1]+duree[iDur],nb)
            cumulAtt += valAtt
            if valAtt > 0 :
                k = 0
                while k < valAtt :
                    xtimeAttente.append(tabA[queue[k]])
                    ynbAttente.append(k+1)
            tabChaine.append(tabA[iArr] + duree[iDur])
            cumulAtt = cumulAtt-1
            iArr += 1
            iDur+= 1

    return xtimeAttente, ynbAttente



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

        print("tableau nombres aleatoires")
        tabAlea = gene_rand(NB_SIM)
        print(tabAlea)
        print(len(tabAlea))


        if self.ui.evtMark.isChecked() :
            print("Markov")
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
            x1 = tabAffichageExpo(tabPoissArr)

        else:
            print("test loi normale")
            tabAlea1 = gene_rand(NB_SIM)
            tabAlea2 = gene_rand(NB_SIM)
            tabNormale = loiNormale(tabAlea1, tabAlea2, LAM_DA)
            print(tabNormale)
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
        xProd, yProd = chaineProd(tabPoissArr, tabPoissTrt, NB_SIM)
        print("Chaine de production")
        print(xProd)
        print(yProd)


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
