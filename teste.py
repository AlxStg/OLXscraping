from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import html
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
import time

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

chrome = webdriver.Chrome(desired_capabilities=capa)
wait = WebDriverWait(chrome, 20)

url = 'https://mg.olx.com.br/belo-horizonte-e-regiao/autos-e-pecas/motos/moto-bmw-gs-650-1027167553?_ga=2.49804390.1518715603.1651148420-1613334648.1640486055'

chrome.get(url)

try:
    teste = chrome.find_element(by=By.XPATH, value = "//head/title").get_attribute('innerHTML')
except:
    teste = 'N/A'

if 'honda' in teste or 'HONDA' in teste or 'yamaha' in teste or 'YAMAHA' in teste or 'suzuki' in teste or 'SUZUKI' in teste or 'DAFRA' in teste or 'dafra' in teste:
    print('sim')
    


else:
    print('não')

chrome.quit()
