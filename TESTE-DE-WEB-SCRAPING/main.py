from funcoes import obterHTML, downloadArquivos, salvaArquivosZip
import re

def main():

    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    arquivos = {'Anexo I': r"\bAnexo I\b", 'Anexo II': r"\bAnexo II\b" }

    print('Web Scraping Iniciando...')
    print('Url: ', url)
    html = obterHTML(url)

    if html.status_code == 200:
        
        pdfs = downloadArquivos(html.text, arquivos)
        
        if len(pdfs) != 0:
            salvaArquivosZip(pdfs, 'Anexos_zip.zip')

if __name__ == "__main__":

    main()