from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from dados_anuncio import pegaDados
import pandas as pd
import csv
import time

def getUrl(paginacao):
    return "https://mg.olx.com.br/belo-horizonte-e-regiao/autos-e-pecas/motos?o="+str(paginacao)+"&pe=8000&ps=2000&re=36&rs=28&sf=1"


# Inicia o browser
inicio = time.time()
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

chrome = webdriver.Chrome(desired_capabilities=capa)
wait = WebDriverWait(chrome, 20)


# Percorre a paginação da categoria para obter os links de todos os anúncios
url_list = []

for i in (range(1, 2)):
    chrome.get(getUrl(i))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-12rk7z2-0')))
    chrome.execute_script("window.stop();")
    
    itens = chrome.find_elements(by=By.CLASS_NAME, value="sc-12rk7z2-0")

    for item in itens:
        item_link = item.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        url_list.append(item_link)
        
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print()
print(f'>>>> {len(url_list)} Links encontrados')
print()
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
chrome.quit()

dados_anuncios = []



#Coleta dados de cada anuncio

contador = 0

for i, url in enumerate(url_list):
    try:
        contador += 1
        if 'olx.com.br' not in url:
            continue
        atrib_anun = pegaDados(url)
        dados_anuncios.append(atrib_anun)
        print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Anuncios coletados: {contador}')
    except:
        continue    
print(dados_anuncios)

#Salva os dados coletados em um arquivo csv
header = ['nome', 'preco_anterior', 'preco', 'imagem', 'ano', 'cilindradas', 'km', 'tipo', 'bairro', 'cidade', 'cep', 'data', 'cod', 'url']

try:
    with open('csv_dct.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for elem in dados_anuncios:
            writer.writerow(elem)
except IOError:
    print("I/O error")

fim = time.time()
print(fim - inicio)