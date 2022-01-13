'''
*****************************************************************************************************************************************
* Programa que calcula, diariamente, o faturamento e a quantidade de produtos vendida no dia anterior a partir de uma planilha no Excel *
* alocada em uma pasta no Google Drive. Além disso, envia um e-mail contendo essas informações.                                         *
*                                                                                                                                       *
* Myke Leony dos Santos Amorim. 10 de janeiro de 2021.                                                                                  *                                                                              *
*****************************************************************************************************************************************
'''

import time
from datetime import date

import pyautogui
import webbrowser

import pandas as pd

pyautogui.PAUSE = 0.5

webbrowser.open_new_tab('https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh')

time.sleep(5)

pyautogui.click(x=412, y=381)   # Seleciona o elemento do arquivo na pasta do drive.
pyautogui.click(x=1161, y=184)  # Clica na select tag que contém o botão de download.
pyautogui.click(x=922, y=622)   # Clica no botão de download do arquivo.

time.sleep(6)   # Espera a conclusão do download.

with pd.ExcelFile(r'/home/linux/Downloads/Vendas - Dez.xlsx') as xlsl:
    tabela = pd.read_excel(xlsl, usecols=['Quantidade', 'Valor Final'])     # Apenas as colunas "Quantidade" e "Valor Final" são relevantes.

    # Cálculos:
    faturamento = tabela['Valor Final'].sum()
    qtd_vendas = tabela['Quantidade'].sum()

# Envio do e-mail contendo as informações das vendas do dia:
webbrowser.open_new_tab('https://mail.google.com/mail/u/0/#inbox')

time.sleep(6)

pyautogui.click(x=122, y=204)   # Abre a caixa de envio de e-mail no Gmail.

time.sleep(6)

pyautogui.write('mykeleony147@gmail.com')
pyautogui.typewrite(['tab', 'tab'], interval=0.5)
pyautogui.write(f'Faturamento e quantidade de produtos vendidos em {date.today()}')     # Assunto do e-mail.
pyautogui.typewrite(['tab'])
pyautogui.write(f'O faturamento em {date.today()} foi de R${str(faturamento)}. O total de produtos vendidos foi de {str(qtd_vendas)} unidades.\n\n Atenciosamente, Myke Amorim.')
pyautogui.typewrite(['tab', 'enter'], interval=0.5)     # Clica no botão de envio.
