from selenium import webdriver
from selenium.webdriver.common.by import By
from dados_anuncio import pegaDados

def getUrl(paginacao):
    return "https://mg.olx.com.br/belo-horizonte-e-regiao/autos-e-pecas/motos?o="+str(paginacao)+"&pe=20000&ps=2000&re=35&rs=18"


# Inicia o browser
chrome = webdriver.Chrome()

# Percorre a paginação da categoria para obter os links de todos os anúncios
url_list = []

for i in (range(1, 2)):
    chrome.get(getUrl(i))
    itens = chrome.find_elements(by=By.CLASS_NAME, value="sc-12rk7z2-0")

    for item in itens:
        item_link = item.find_element(
            by=By.TAG_NAME, value='a').get_attribute('href')
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
item_index = 0
for i, url in enumerate(url_list):
    if 'olx.com.br' not in url:
        continue
    atrib_anun = pegaDados(url)
    print (atrib_anun)
    dados_anuncios.append(atrib_anun)
print(dados_anuncios)