# coding=utf-8
# Importation des Librairies
from PyQt4.QtGui import *
from pylab import *
import matplotlib.pyplot as plt
import random as rand

import interSimu
from interSimu import Ui_MainWindow

# Nombre de simulation
NB_SIM = 100

# Genere une liste de nombre aléatoire de taille NB_SIM en utilisant la fonction random de python
def gene_rand():
    #Genere 100 nombres aleatoires a 4 decimales
    l = [round(rand.random(),4) for i in range(NB_SIM)]
    return l

# Genere une liste de nombre suivant une loi exponentielle prenant en paramètre une liste de nombre aléatoire et lambda
def loiExpo(tabAlea, lambd):
    res = [round((-math.log(i)/lambd),4) for i in tabAlea]
    return res

# Genere une liste suivant une loi exponentielle theorique en utilisant la fonction expovariate de la bibliotheque random
# Prend en parametre lambda
def loiExpoTheorique(lambd):
    resExpoTheo = []
    i = 0
    for i in range(NB_SIM):
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
def tabRaie():
    resRaie = []
    for i in range(NB_SIM):
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
        print(self.ui.nbEvt.toPlainText())
        x=[0,10,100]
        y=[3,4,5]

        self.ui.graphArrivee.axes.set_xscale('log') # Nothing Happens
        self.ui.graphArrivee.axes.set_title('GRAPH') # Nothing Happens

        self.ui.graphArrivee.axes.plot(x,y)
        self.ui.graphArrivee.draw()


# Fonction main
if __name__=="__main__":
    # Appel de l'interface
    app = QApplication(sys.argv)
    applicationViewer = ApplicationViewer()
    applicationViewer.show()
    app.exec_()

    print("tableau nombres aleatoires")
    tabAlea = gene_rand()
    print(tabAlea)
    print(len(tabAlea))

    print("______________")
    print("loi exponentielle")

    tabExp = loiExpo(tabAlea, 0.05)
    print(tabExp)

    print("______________")
    print("loi exponentielle theorique")
    tabExpoTheorique = loiExpoTheorique(0.05)
    print(tabExpoTheorique)
    
    print("______________")
    print("tableau exponentionel trie")
    tabExp.sort()
    print(tabExp)

    print("______________")
    print("tableau expo theorique trie")
    tabExpoTheorique.sort()
    print(tabExpoTheorique)

    print("______________")
    print("tableau processus poisson")
    tabPoiss = processPoi(tabExp)
    print(tabPoiss)

    print("______________")
    print("tableau representant les raies")
    tabRaie = tabRaie()
    print(tabRaie)

    print("______________")
    print("Tableau test")
    tabStyle = tabAffichageExpo(tabExp)
    print(tabStyle)

    print "voici la val de ton champ :"

    # Traçage du graphique
    plt.plot(tabStyle, tabRaie)
    plt.show()
