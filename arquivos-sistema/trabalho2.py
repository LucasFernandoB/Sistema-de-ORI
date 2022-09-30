from cabecalho import *
import os
from arquivo import *
from time import sleep

arq='palavrasSeparadas.txt'
arq1='texto1.txt'
arq2='texto2.txt'
arq3='texto3.txt'
arq4='texto4.txt'
arq5='texto5.txt'
arq6='texto6.txt'
arq7='texto7.txt'
txtaux='txtAux.txt'

texto1='doc1.txt'
texto2='doc2.txt'
texto3='doc3.txt'
texto4='doc4.txt'
texto5='doc5.txt'
texto6='doc6.txt'
texto7='doc7.txt'

if not arquivoExiste(txtaux):
    criarArquivo(txtaux)
if not arquivoExiste(arq):
    criarArquivo(arq)
if not arquivoExiste(arq1):
    criarArquivo(arq1)
if not arquivoExiste(arq2):
    criarArquivo(arq2)
if not arquivoExiste(arq3):
    criarArquivo(arq3)
if not arquivoExiste(arq4):
    criarArquivo(arq4)
if not arquivoExiste(arq4):
    criarArquivo(arq)
if not arquivoExiste(arq5):
    criarArquivo(arq5)
if not arquivoExiste(arq6):
    criarArquivo(arq6)
if not arquivoExiste(arq7):
    criarArquivo(arq7)
if not arquivoExiste(texto1):
    criarArquivo(texto1)
if not arquivoExiste(texto2):
    criarArquivo(texto2)
if not arquivoExiste(texto3):
    criarArquivo(texto3)
if not arquivoExiste(texto4):
    criarArquivo(texto4)
if not arquivoExiste(texto5):
    criarArquivo(texto5)
if not arquivoExiste(texto6):
    criarArquivo(texto6)
if not arquivoExiste(texto7):
    criarArquivo(texto7)

ajuda=[]
while True:
    resposta = menu(['Pesquizar Palavra e Ranquear','Procurar ocorrencia no documento','SAIR'])
    if resposta == 1:
        separarPalavras(arq, arq1, arq2, arq3,arq4,arq5,arq6,arq7,txtaux)
        lerQuantidade(txtaux)
        lerArquivoMatriz(arq)
    elif resposta==2:
        buscaDocumento(texto1, texto2, texto3, texto4,texto5,texto6,texto7)
    else:
        cabecalho('PROGRAMA FINALIZADO!')
        break
        sleep(1)
    print("\n"*10)
