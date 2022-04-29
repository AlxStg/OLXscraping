from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import html




chrome = webdriver.Chrome('chromedriver.exe')
chrome.get('https://mg.olx.com.br/belo-horizonte-e-regiao/autos-e-pecas/motos/cbx-250-twister-2004-1025885445')

json_iten = chrome.find_element(by=By.ID, value="initial-data")
atrib_json = json_iten.get_attribute('data-json')
saida = html.escape(atrib_json)
conv = html.unescape(saida)
chrome.quit()
print('>>>>>>>>>SAÍDA<<<<<<<<<')
anuncio = json.loads(conv)

preco = anuncio['ad']["priceValue"]
print(preco)

