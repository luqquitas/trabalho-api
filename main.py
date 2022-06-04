from xmlrpc.client import boolean
from PyQt5 import  uic
import PyQt5.QtWidgets as QtWidgets

import sys
import requests
import json


#autores Arthur Zaneti, Érick Matos e Lucas Cherobin
# Trabalho API de Moedas com PYQT 

class Ui(QtWidgets.QDialog):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(R"opcoes.ui", self)
        self.show()

        self.cotaButton.clicked.connect(self.handleCotaButton)
        self.fechamentoButton.clicked.connect(self.handleFechamentoButton)
        self.cotallButton.clicked.connect(self.handleCotallButton)
        self.conversaoButton.clicked.connect(self.handleConversaoButton)

    def handleFechamentoButton(self):
        super(Ui, self).__init__()
        uic.loadUi(R"fechamento.ui", self)
        self.show()

        self.consultafechamento.clicked.connect(self.handleConsultaFechamento)
        self.limparFechamentoButton.clicked.connect(self.handleLimparFechamentoButton)

    def handleCotaButton(self):

        super(Ui, self).__init__()
        uic.loadUi(R"cotacao.ui", self)
        self.show()

        self.consultacotacao.clicked.connect(self.handleConsultaCota)
        self.limparcotacao.clicked.connect(self.handleLimparCotaButton)

    def handleCotallButton(self):
        super(Ui, self).__init__()
        uic.loadUi(R"cotall.ui", self)
        self.show()
        self.consultaButton.clicked.connect(self.handleConsultaAll)
        
    def handleConversaoButton(self):
    
        super(Ui, self).__init__()
        uic.loadUi(R"conversao.ui", self)
        self.show()

        self.consultaconversao.clicked.connect(self.handleConsultaConversao)
        self.limparconversao.clicked.connect(self.handleLimparConversaoButton)

        
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
        outputText = ''

        valor = contentJson["USD"]["ask"]
        cod = contentJson["USD"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["CAD"]["ask"]
        cod = contentJson["CAD"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["EUR"]["ask"]
        cod = contentJson["EUR"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["ARS"]["ask"]
        cod = contentJson["ARS"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["BTC"]["ask"]
        cod = contentJson["BTC"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["LTC"]["ask"]
        cod = contentJson["LTC"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["JPY"]["ask"]
        cod = contentJson["JPY"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["CHF"]["ask"]
        cod = contentJson["CHF"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["AUD"]["ask"]
        cod = contentJson["AUD"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["CNY"]["ask"]
        cod = contentJson["CNY"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["ILS"]["ask"]
        cod = contentJson["ILS"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["ETH"]["ask"]
        cod = contentJson["ETH"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["XRP"]["ask"]
        cod = contentJson["XRP"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'

        valor = contentJson["DOGE"]["ask"]
        cod = contentJson["DOGE"]["code"]
        outputText += f'Moeda {cod}: {valor}\n'


        self.conteudoTextBrowser.setText(outputText)
        
    def handleConsultaCota(self):
        
        inputmoeda = self.moedaTextEdit.toPlainText()
        inputmoeda_2 = self.moeda_2TextEdit.toPlainText()

        if inputmoeda == '' and inputmoeda_2 == None:
            return
        
        reqURL = f'https://economia.awesomeapi.com.br/{inputmoeda}-{inputmoeda_2}'
        print(reqURL)

        response = requests.get(reqURL)

        contentJson = json.loads(response.content)

        valor = []
        outputText = ''
        
        for dia in contentJson:
            
            valor = dia["ask"]
            
            outputText += f'{inputmoeda.upper()} - {inputmoeda_2.upper()}: {valor}\n'

        self.conteudoTextBrowser.setText(outputText)
    
    def handleLimparCotaButton(self):
        self.moedaTextEdit.setText('')
        self.moeda_2TextEdit.setText('')
        self.conteudoTextBrowser.setText('')
        
    def handleConsultaConversao(self):
        
        inputmoeda = self.moedaTextEdit.toPlainText()
        inputmoeda_2 = self.moeda_2TextEdit.toPlainText()
        inputvalor = float(self.valorTextEdit.toPlainText())

        if inputmoeda == '' and inputmoeda_2 == None and inputvalor == None:
            return
        
        reqURL = f'https://economia.awesomeapi.com.br/{inputmoeda}-{inputmoeda_2}'
        print(reqURL)

        response = requests.get(reqURL)

        contentJson = json.loads(response.content)

        valor = []
        soma = 0
        outputText = ''
        
        for dia in contentJson:
            
            valor = float(dia["ask"])
            
            soma = valor * inputvalor
            
            print(valor + soma)
            
            outputText += f'Na cotação de {valor: .2f}, a quantida de {inputvalor} {inputmoeda.upper()} equivale a {soma: .2f} {inputmoeda_2.upper()}\n'

        self.conteudoTextBrowser.setText(outputText)
    
    def handleLimparConversaoButton(self):
        self.moedaTextEdit.setText('')
        self.moeda_2TextEdit.setText('')
        self.valorTextEdit.setText('')
        self.conteudoTextBrowser.setText('')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()