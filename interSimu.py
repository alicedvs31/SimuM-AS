# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interSimu.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1130, 910)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 20, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 80, 821, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.confEvt = QtGui.QLabel(self.groupBox)
        self.confEvt.setGeometry(QtCore.QRect(40, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.confEvt.setFont(font)
        self.confEvt.setObjectName(_fromUtf8("confEvt"))
        self.nbEvt = QtGui.QPlainTextEdit(self.groupBox)
        self.nbEvt.setGeometry(QtCore.QRect(210, 50, 71, 31))
        self.nbEvt.setObjectName(_fromUtf8("nbEvt"))
        self.cfLambdAr = QtGui.QLabel(self.groupBox)
        self.cfLambdAr.setGeometry(QtCore.QRect(330, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.cfLambdAr.setFont(font)
        self.cfLambdAr.setObjectName(_fromUtf8("cfLambdAr"))
        self.varLambdArr = QtGui.QPlainTextEdit(self.groupBox)
        self.varLambdArr.setGeometry(QtCore.QRect(450, 50, 71, 31))
        self.varLambdArr.setObjectName(_fromUtf8("varLambdArr"))
        self.confTemps = QtGui.QLabel(self.groupBox)
        self.confTemps.setGeometry(QtCore.QRect(560, 50, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.confTemps.setFont(font)
        self.confTemps.setObjectName(_fromUtf8("confTemps"))
        self.validPara = QtGui.QCommandLinkButton(self.groupBox)
        self.validPara.setGeometry(QtCore.QRect(610, 100, 101, 41))
        self.validPara.setObjectName(_fromUtf8("validPara"))
        self.varLambdTrt = QtGui.QPlainTextEdit(self.groupBox)
        self.varLambdTrt.setGeometry(QtCore.QRect(710, 50, 71, 31))
        self.varLambdTrt.setObjectName(_fromUtf8("varLambdTrt"))
        self.evtMark = QtGui.QCheckBox(self.groupBox)
        self.evtMark.setGeometry(QtCore.QRect(50, 110, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.evtMark.setFont(font)
        self.evtMark.setObjectName(_fromUtf8("evtMark"))
        self.graphArrivee = MatplotlibWidget(self.centralwidget)
        self.graphArrivee.setGeometry(QtCore.QRect(30, 270, 1061, 181))
        self.graphArrivee.setObjectName(_fromUtf8("graphArrivee"))
        self.graphTrait = MatplotlibWidget(self.centralwidget)
        self.graphTrait.setGeometry(QtCore.QRect(30, 490, 1061, 181))
        self.graphTrait.setObjectName(_fromUtf8("graphTrait"))
        self.graphProd = MatplotlibWidget(self.centralwidget)
        self.graphProd.setGeometry(QtCore.QRect(30, 700, 1061, 181))
        self.graphProd.setObjectName(_fromUtf8("graphProd"))
        self.confEvt_2 = QtGui.QLabel(self.centralwidget)
        self.confEvt_2.setGeometry(QtCore.QRect(30, 250, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.confEvt_2.setFont(font)
        self.confEvt_2.setObjectName(_fromUtf8("confEvt_2"))
        self.confEvt_3 = QtGui.QLabel(self.centralwidget)
        self.confEvt_3.setGeometry(QtCore.QRect(30, 470, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.confEvt_3.setFont(font)
        self.confEvt_3.setObjectName(_fromUtf8("confEvt_3"))
        self.confEvt_4 = QtGui.QLabel(self.centralwidget)
        self.confEvt_4.setGeometry(QtCore.QRect(30, 680, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.confEvt_4.setFont(font)
        self.confEvt_4.setObjectName(_fromUtf8("confEvt_4"))
        self.groupBox.raise_()
        self.label_4.raise_()
        self.graphArrivee.raise_()
        self.graphTrait.raise_()
        self.graphProd.raise_()
        self.confEvt_2.raise_()
        self.confEvt_3.raise_()
        self.confEvt_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation postes de fabrication", None))
        self.label_4.setText(_translate("MainWindow", "Simulation postes de fabrication", None))
        self.groupBox.setTitle(_translate("MainWindow", "Paramètres de simulation", None))
        self.confEvt.setText(_translate("MainWindow", "Nombre d\'évènements : ", None))
        self.cfLambdAr.setText(_translate("MainWindow", "Lambda arrivées :", None))
        self.confTemps.setText(_translate("MainWindow", "Lambda traitements : ", None))
        self.validPara.setText(_translate("MainWindow", "Valider", None))
        self.evtMark.setText(_translate("MainWindow", "Environnement Markovien", None))
        self.confEvt_2.setText(_translate("MainWindow", "Arrivée des pièces sur le tapis", None))
        self.confEvt_3.setText(_translate("MainWindow", "Temps de traitement par pièce", None))
        self.confEvt_4.setText(_translate("MainWindow", "Chaine de production", None))

from matplotlibwidget import MatplotlibWidget
