# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Lucas Cherobin\Documents\GitHub\trabalho-api\opcoes.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Lucas Cherobin\\Documents\\GitHub\\trabalho-api\\../../../Desktop/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.cotaButton = QtWidgets.QPushButton(Dialog)
        self.cotaButton.setGeometry(QtCore.QRect(20, 70, 361, 28))
        self.cotaButton.setObjectName("cotaButton")
        self.fechamentoButton = QtWidgets.QPushButton(Dialog)
        self.fechamentoButton.setGeometry(QtCore.QRect(20, 110, 361, 28))
        self.fechamentoButton.setObjectName("fechamentoButton")
        self.cotallButton = QtWidgets.QPushButton(Dialog)
        self.cotallButton.setGeometry(QtCore.QRect(20, 150, 361, 28))
        self.cotallButton.setObjectName("cotallButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Menu"))
        self.cotaButton.setText(_translate("Dialog", "1 - Cotação"))
        self.fechamentoButton.setText(_translate("Dialog", "2 - Fechamento"))
        self.cotallButton.setText(_translate("Dialog", "3 - Cotação de Todas Moedas"))
