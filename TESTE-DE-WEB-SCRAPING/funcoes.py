from bs4 import BeautifulSoup
import requests
import zipfile as zp
import re
import os

def obterHTML(url):

    #Estabelece a requisição HTTP com a url usando o método get
    resposta = requests.get(url)

    if resposta.status_code == 200:
        print("Requisição estabelecida com sucesso!")
    else:
        print("Erro: ", resposta.status_code)
    
    return resposta


def downloadArquivos(html, arquivos):

    soup = BeautifulSoup(html, 'html.parser')

    pdfs = []
    for link in soup.find_all('a', href = True):
        for chave, valor in arquivos.items():
            if re.search(valor, link.text) and link["href"].endswith(".pdf"):

                arquivo = requests.get(link["href"])
                if arquivo.status_code == 200:

                    with open(chave + ".pdf", "wb") as file:
                        file.write(arquivo.content)

                    pdfs.append(chave + ".pdf")
                    print("Download ", chave + ".pdf", "concluído com sucesso!")

                else:
                    print("Download ", chave + ".pdf", "falhou! Erro: ", arquivo.status_code)
    
    return pdfs

                


def salvaArquivosZip(arquivos, nome_arquivo_zip):

    with zp.ZipFile(nome_arquivo_zip, 'w') as zip:
        for arquivo in arquivos:
            zip.write(arquivo, arcname = arquivo)

            #Deleta os arquivos que foram compactados
            if os.path.exists(arquivo):
                os.remove(arquivo)

    print("Arquivos compactados em Zip com sucesso!")



