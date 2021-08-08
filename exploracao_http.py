'''
Programa que se conecta e extrai dados manualmente de uma pagina web.
Myke Leony dos Santos Amorim. 01 maio de 2021.
'''

import socket

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete.connect( ('data.pr4e.org', 80) )                    #Conectando à porta 80 (servidor web) do aplicativo (site) data.pr4e.org

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()   #Com o comando GET no software, é requisitado um documento lá contido.
soquete.send(cmd)                                                            #Enviando o comando especificado ao servidor conectado.

while True:
    dados = soquete.recv(512)                           #Recebendo e armazenando 512 caracteres de dados do software ao qual o socket está conectado.

    if(len(dados) < 1):                                 #Caso o tamanho do dado recebido seja 0, não há mais conteúdo e a conexão é encerrada.
        break

    print(dados.decode(), end = '')                    #Imprimindo os dados recebidos.

soquete.close()     #Encerrando a conexão com o aplicativo.
