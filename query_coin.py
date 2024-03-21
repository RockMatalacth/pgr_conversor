#IMPORTAÇÃO DE MÓDULO
import requests #Requests é uma biblioteca de Python usada para fazer solicitações HTTP, como: GET, POS, PUT, DELETE. Muito utilizada para interagir com APIs da web.

import Json_dolar
import Json_Bitcoin

#REQUISIÇÕES
requisicao1 = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL') #formato de renderização para trazer informação de uma página 
requisicao2 = requests.get('https://economia.awesomeapi.com.br/all/BTC-USD') #formato de renderização para trazer informação de uma página 

cotacao1 = requisicao1.json()
cotacao2 = requisicao2.json()


dolar_real = float(cotacao1['USD']['bid'])
bitcoin_dolar = float(cotacao2['BTC']['bid'])
valor_bitcoin_real = dolar_real * bitcoin_dolar

#Impressão 
print('\nCOTAÇÃO DOLAR\n')
print('Moeda:', cotacao1['USD']['name'])
print('Valor da cotação: R$', cotacao1['USD']['bid'])

print('\n\n--------------\n\n')

print('COTAÇÃO BOTCOIN\n')
print('Moeda:', cotacao2['BTC']['name'])
print('Valor da cotação: $', cotacao2['BTC']['bid'])

print('\n\n--------------\n\n')

print('\nBITCOIN EM REAL\n')
print(f'O valor do bitcoin em reais é: R$ {valor_bitcoin_real} reais\n')
