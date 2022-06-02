from xmlrpc.client import boolean
from PyQt5 import  uic
import PyQt5.QtWidgets as QtWidgets

import sys
import requests
import json

class Ui(QtWidgets.QDialog):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(R"C:\Users\Lucas Cherobin\Documents\GitHub\trabalho-api\opcoes.ui", self)
        self.show()

        self.cotaButton.clicked.connect(self.handleCotaButton)
        self.fechamentoButton.clicked.connect(self.handleFechamentoButton)
        self.cotallButton.clicked.connect(self.handleCotallButton)

    def handleFechamentoButton(self):
        super(Ui, self).__init__()
        uic.loadUi(R"C:\Users\Lucas Cherobin\Documents\GitHub\trabalho-api\fechamento.ui", self)
        self.show()

        self.consultafechamento.clicked.connect(self.handleConsultaFechamento)
        self.limparFechamentoButton.clicked.connect(self.handleLimparFechamentoButton)

    def handleCotaButton(self):

        super(Ui, self).__init__()
        uic.loadUi(R"C:\Users\Lucas Cherobin\Documents\GitHub\trabalho-api\cotacao.ui", self)
        self.show()

        #self.consultaButton.clicked.connect(self.handleCotaButton)
        #self.limparButton.clicked.connect(self.handleLimparButton)

    def handleCotallButton(self):
        super(Ui, self).__init__()
        uic.loadUi(R"C:\Users\Lucas Cherobin\Documents\GitHub\trabalho-api\cotall.ui", self)
        self.show()
        self.consultaButton.clicked.connect(self.handleConsultaAll)

        
    def handleConsultaFechamento(self):
        inputmoeda = self.moedaTextEdit.toPlainText()
        inputday = int(self.dayTextEdit.toPlainText())

        if inputmoeda == '' and inputday == None:
            return
        
        reqURL = f'https://economia.awesomeapi.com.br/json/daily/{inputmoeda}-BRL/{inputday}'
        print(reqURL)

        response = requests.get(reqURL)

        contentJson = json.loads(response.content)

        valor = []
        outputText = ''
        dias = 0
        
        for dia in contentJson:
            
            valor = dia["ask"]

            dias = dias + 1
            
            outputText += f'Dia {dias} - {inputmoeda.upper()}: {valor}\n'

        self.conteudoTextBrowser.setText(outputText)

    def handleLimparFechamentoButton(self):
        self.moedaTextEdit.setText('')
        self.dayTextEdit.setText('')
        self.conteudoTextBrowser.setText('')

    def handleConsultaAll(self):        
        reqURL = f'https://economia.awesomeapi.com.br/json/all'
        print(reqURL)

        response = requests.get(reqURL)

        contentJson = json.loads(response.content)

        valor = contentJson["ask"]

        cod = contentJson["code"]
        
        outputText += f'Código {cod}: {valor}\n'

        self.conteudoTextBrowser.setText(outputText)

#teste

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()