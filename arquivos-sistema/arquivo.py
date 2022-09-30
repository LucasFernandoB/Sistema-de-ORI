from cabecalho import *
import math
import os


# funcao pra ver se o arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# funcao pra criar o arquivo caso ele nao exista
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# funcao apenas para mostrar os dados do arquivo separado
def lerArquivoMatriz(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir arquivo')
    else:
        cabecalho1(' PALAVRAS ARRUMADAS \n')
        for linha in a:
            dado = linha.split('\n')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<14} ')
    finally:
        print('\n')
        a.close()

def lerQuantidade(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir arquivo')
    else:
        cabecalho1('\nPALAVRAS        DOC1       DOC2       DOC3       DOC4       DOC5       DOC6       DOC7 \n')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<14} {dado[1]:>3}{dado[2]:>11}{dado[3]:>11}{dado[4]:>11}{dado[5]:>11}{dado[6]:>11}{dado[7]:>11}')
    finally:
        print('\n')
        a.close()

def buscaDocumento(arquivo1, arquivo2, arquivo3,arquivo4,arquivo5,arquivo6,arquivo7):
    try:
        a1 = open(arquivo1, 'rt')
        a2 = open(arquivo2, 'rt')
        a3 = open(arquivo3, 'rt')
        a4 = open(arquivo4, 'rt')
        a5 = open(arquivo5, 'rt')
        a6 = open(arquivo6, 'rt')
        a7 = open(arquivo7, 'rt')
    except:
        print('Houve um erro na abertura em um dos arquivos')
    else:
        texto = str(input('Texto: '))
        termos=[]
        aux=0
        con=0
        for linha in a1:
            if con<3:
                ajuda=linha.strip('\n')
                termos.append(ajuda)
            con=con+1
            linha=linha.lower().strip(",").strip("?")
            t=texto.lower()
            te=t.split(" ")
            for palavra in te:
                if palavra in linha:
                    aux=1
        if aux == 1:
            print("doc1 ->", termos)

        con=0
        termos.clear()
        for linha in a2:
            if con<3:
                ajuda=linha.strip('\n')
                termos.append(ajuda)
            con=con+1
            linha = linha.lower().strip(",").strip("?")
            t = texto.lower()
            te = t.split(" ")
            for palavra in te:
                if palavra in linha:
                    aux=2
        if aux == 2:
            print("doc2 ->",termos)

        con=0
        termos.clear()
        for linha in a3:
            if con<3:
                ajuda=linha.strip('\n')
                termos.append(ajuda)
            con=con+1
            linha = linha.lower().strip(",").strip("?")
            t = texto.lower()
            te = t.split(" ")
            for palavra in te:
                if palavra in linha:
                    aux=3
        if aux == 3:
            print("doc3 ->",termos)

        con = 0
        termos.clear()
        for linha in a4:
            if con < 3:
                ajuda = linha.strip('\n')
                termos.append(ajuda)
            con = con + 1
            linha = linha.lower().strip(",").strip("?")
            t = texto.lower()
            te = t.split(" ")
            for palavra in te:
                if palavra in linha:
                    aux = 4
        if aux == 4:
            print("doc4 ->", termos)

        con = 0
        termos.clear()
        for linha in a5:
            if con < 3:
                ajuda = linha.strip('\n')
                termos.append(ajuda)
            con = con + 1
            linha = linha.lower().strip(",").strip("?")
            t = texto.lower()
            te = t.split(" ")
            for palavra in te:
                if palavra in linha:
                    aux = 5
        if aux == 5:
            print("doc5 ->", termos)

        con = 0
        termos.clear()
        for linha in a6:
            if con < 3:
                ajuda = linha.strip('\n')
                termos.append(ajuda)
            con = con + 1
            linha = linha.lower().strip(",").strip("?")
            t = texto.lower()
            te = t.split(" ")
            for palavra in te:
                if palavra in linha:
                    aux = 6
        if aux == 6:
            print("doc6 ->", termos)

        con = 0
        termos.clear()
        for linha in a7:
            if con < 3:
                ajuda = linha.strip('\n')
                termos.append(ajuda)
            con = con + 1
            linha = linha.lower().strip(",").strip("?")
            t = texto.lower()
            te = t.split(" ")
            for palavra in te:
                if palavra in linha:
                    aux = 7
        if aux == 7:
            print("doc7 ->", termos)



        if aux==0:
            print("Palavra nao encontrada nos documentos.")

    a1.close()
    a2.close()
    a3.close()
    a4.close()
    a5.close()
    a6.close()
    a7.close()






# funcao pra apenas listar cada arquivo de texto separado
def lerBusca(conjunto):
    for linha in conjunto:
        dado = linha.split('\n')
        print(dado[0])

# funcao que separa as palavras
def separarPalavras(arq, arquivo1, arquivo2, arquivo3,arquivo4,arquivo5,arquivo6,arquivo7,txtaux):
    try:
        a1 = open(arquivo1, 'rt')
        a2 = open(arquivo2, 'rt')
        a3 = open(arquivo3, 'rt')
        a4 = open(arquivo4, 'rt')
        a5 = open(arquivo5, 'rt')
        a6 = open(arquivo6, 'rt')
        a7 = open(arquivo7, 'rt')
    except:
        print('Houve um erro na abertura em um dos arquivos')
    else:
        try:
            a = open(arq, 'w')
            txt=open(txtaux,'w')
        except:
            print('Houve um erro na abertura de arquivo')
        else:
            try:
                doc1 = []
                doc2 = []
                doc3 = []
                doc4 = []
                doc5 = []
                doc6 = []
                doc7 = []
                vetorTermo = []
                vetorQtd=[]
                termos=[]
                tfIdf=[]
                con=1
                aux=[]

                for linha in a1:  # faco a leitura das palavras ja lematizadas
                    dado = linha.split('\n')
                    palavra = dado[0]
                    doc1.append(palavra)
                    vetorTermo.append(palavra)
                for linha in a2:  # faco a leitura das palavras lematizadas
                    dado = linha.split('\n')
                    palavra = dado[0]
                    doc2.append(palavra)
                    vetorTermo.append(palavra)
                for linha in a3:  # faco a leitura das palavras lematizadas
                    dado = linha.split('\n')
                    palavra = dado[0]
                    doc3.append(palavra)
                    vetorTermo.append(palavra)
                for linha in a4:  # faco a leitura das palavras lematizadas
                    dado = linha.split('\n')
                    palavra = dado[0]
                    doc4.append(palavra)
                    vetorTermo.append(palavra)
                for linha in a5:  # faco a leitura das palavras lematizadas
                    dado = linha.split('\n')
                    palavra = dado[0]
                    doc5.append(palavra)
                    vetorTermo.append(palavra)
                for linha in a6:  # faco a leitura das palavras lematizadas
                    dado = linha.split('\n')
                    palavra = dado[0]
                    doc6.append(palavra)
                    vetorTermo.append(palavra)
                for linha in a7:  # faco a leitura das palavras lematizadas
                    dado = linha.split('\n')
                    palavra = dado[0]
                    doc7.append(palavra)
                    vetorTermo.append(palavra)

                termos=sorted(set(vetorTermo))# elimino as repetidas e ordeno

                for palavra in termos:
                    # quantas veses cada palavra repete nos documentos
                    vetorQtd.append(doc1.count(palavra))
                    vetorQtd.append(doc2.count(palavra))
                    vetorQtd.append(doc3.count(palavra))
                    vetorQtd.append(doc4.count(palavra))
                    vetorQtd.append(doc5.count(palavra))
                    vetorQtd.append(doc6.count(palavra))
                    vetorQtd.append(doc7.count(palavra))

                    txt.write(f'{palavra};{vetorQtd[0]};{vetorQtd[1]};{vetorQtd[2]};{vetorQtd[3]};{vetorQtd[4]};{vetorQtd[5]};{vetorQtd[6]}\n')

                    idf=vetorQtd.count(0)
                    idf=7-idf
                    idf=round((math.log10(7/idf)),7)
                    i=0
                    for x in vetorQtd:
                        if x == 0:
                            vetorQtd[i] = 0
                        else:
                            vetorQtd[i] = round(((math.log10(vetorQtd[i])+ 1)*idf),7)
                        i=i+1

                    tfIdf.append(vetorQtd[0])
                    tfIdf.append(vetorQtd[1])
                    tfIdf.append(vetorQtd[2])
                    tfIdf.append(vetorQtd[3])
                    tfIdf.append(vetorQtd[4])
                    tfIdf.append(vetorQtd[5])
                    tfIdf.append(vetorQtd[6])
                    a.write(f'{palavra} ; {idf} ; {vetorQtd[0]} ; {vetorQtd[1]} ; {vetorQtd[2]} ; {vetorQtd[3]} ; {vetorQtd[4]} ; {vetorQtd[5]} ; {vetorQtd[6]} \n')
                    vetorQtd.clear()
                    i=0
                k=0
                ranqueamento=[]
                texto = str(input('Texto: '))
                t = texto.lower()
                te = t.split(" ")
                print("\n")
                print("Palavras      TF.IDF")
                print("_" * 20)
                indice=0
                ranqueamento=[0]*7


                for palavra in te:
                    if(palavra in termos):
                        indice = termos.index(palavra)
                        posicao=indice*7
                        fim=posicao+6
                        auxi=0
                        while (posicao <= fim):
                            ranqueamento[auxi] += tfIdf[posicao]
                            auxi=auxi+1
                            posicao=posicao+1

                        posicao = 0
                        auxi = 0
                        fim=0
                        indice=0

                print(ranqueamento)













            except:
                print('Houve um erro na hora de escrever os dados')

        a.close()
        a1.close()
        a2.close()
        a3.close()
        a4.close()
        a5.close()
        a6.close()
        a7.close()
        txt.close()
