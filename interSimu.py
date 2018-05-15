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
        MainWindow.resize(1130, 690)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 20, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 80, 751, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.confEvt = QtGui.QLabel(self.groupBox)
        self.confEvt.setGeometry(QtCore.QRect(50, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.confEvt.setFont(font)
        self.confEvt.setObjectName(_fromUtf8("confEvt"))
        self.nbEvt = QtGui.QPlainTextEdit(self.groupBox)
        self.nbEvt.setGeometry(QtCore.QRect(190, 50, 71, 31))
        self.nbEvt.setObjectName(_fromUtf8("nbEvt"))
        self.confLambda = QtGui.QLabel(self.groupBox)
        self.confLambda.setGeometry(QtCore.QRect(320, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.confLambda.setFont(font)
        self.confLambda.setObjectName(_fromUtf8("confLambda"))
        self.varLambda = QtGui.QPlainTextEdit(self.groupBox)
        self.varLambda.setGeometry(QtCore.QRect(380, 50, 71, 31))
        self.varLambda.setObjectName(_fromUtf8("varLambda"))
        self.confTemps = QtGui.QLabel(self.groupBox)
        self.confTemps.setGeometry(QtCore.QRect(510, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.confTemps.setFont(font)
        self.confTemps.setObjectName(_fromUtf8("confTemps"))
        self.validPara = QtGui.QCommandLinkButton(self.groupBox)
        self.validPara.setGeometry(QtCore.QRect(610, 100, 101, 41))
        self.validPara.setObjectName(_fromUtf8("validPara"))
        self.varTemps = QtGui.QPlainTextEdit(self.groupBox)
        self.varTemps.setGeometry(QtCore.QRect(620, 50, 71, 31))
        self.varTemps.setObjectName(_fromUtf8("varTemps"))
        self.graphArrivee = MatplotlibWidget(self.centralwidget)
        self.graphArrivee.setGeometry(QtCore.QRect(30, 250, 1061, 181))
        self.graphArrivee.setObjectName(_fromUtf8("graphArrivee"))
        self.graphTrait = MatplotlibWidget(self.centralwidget)
        self.graphTrait.setGeometry(QtCore.QRect(30, 470, 1061, 181))
        self.graphTrait.setObjectName(_fromUtf8("graphTrait"))
        self.groupBox.raise_()
        self.label_4.raise_()
        self.graphArrivee.raise_()
        self.graphTrait.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation postes de fabrication", None))
        self.label_4.setText(_translate("MainWindow", "Simulation processus de Poisson", None))
        self.groupBox.setTitle(_translate("MainWindow", "Paramètres de simulation", None))
        self.confEvt.setText(_translate("MainWindow", "Nombre d\'évènements : ", None))
        self.confLambda.setText(_translate("MainWindow", "Lambda : ", None))
        self.confTemps.setText(_translate("MainWindow", "Période de temps : ", None))
        self.validPara.setText(_translate("MainWindow", "Valider", None))

from matplotlibwidget import MatplotlibWidget
