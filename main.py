from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd


def getUrl(paginacao):
    return "https://mg.olx.com.br/belo-horizonte-e-regiao/autos-e-pecas/motos?o="+str(paginacao)+"&pe=20000&ps=2000&re=35&rs=18"


def dictToCsv(item_dic):
    '''
    Coloca o conjunto de daodos no formato correto e o salva em um arquivo '.csv'

    param dara_frame item_dic: O conjunto de dados contendo todos os anúncios
    '''
    csv = []
    print(item_dic)
    # Salvando os itens em um csv
    for i in range(len(item_dic)):
        csv.append([])

        if 'Categoria' in item_dic[i]:
            csv[i].append(item_dic[i]['Categoria'])
        else:
            csv[i].append(float('NaN'))
        if 'Modelo' in item_dic[i]:
            csv[i].append(item_dic[i]['Modelo'])
        else:
            csv[i].append(float('NaN'))
        if 'Cilindrada' in item_dic[i]:
            csv[i].append(item_dic[i]['Cilindrada'])
        else:
            csv[i].append(float('NaN'))
        if 'Quilometragem' in item_dic[i]:
            csv[i].append(item_dic[i]['Quilometragem'])
        else:
            csv[i].append(float('NaN'))
        if 'Ano' in item_dic[i]:
            csv[i].append(item_dic[i]['Ano'])
        else:
            csv[i].append(float('NaN'))
        if 'url' in item_dic[i]:
            csv[i].append(item_dic[i]['url'])
        else:
            csv[i].append(float('NaN'))
        if 'preco' in item_dic[i]:
            csv[i].append(item_dic[i]['preco'])
        else:
            csv[i].append(float('NaN'))
        header = ['categoria', 'modelo', 'cilindrada',
                  'quilometragem', 'ano', 'url', 'preco']

        pd.DataFrame(csv).to_csv('olx_data.csv', header=header, index=False)


# Inicia o browser
chrome = webdriver.Chrome()
# Percorre a paginação da categoria para obter os links de todos os anúncios
url_list = []


chrome.get(getUrl(1))
itens = chrome.find_elements(by=By.CLASS_NAME, value="sc-12rk7z2-0")
    
print(itens)
#  "sc-12rk7z2-0 bDLpyo"

for item in itens:
    item_link = item.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
    url_list.append(item_link)

print(url_list)

chrome.quit()