from distutils.log import error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from dados_anuncio import pegaDados
import csv
import time
from datetime import datetime

def getUrl(paginacao):
    return "https://mg.olx.com.br/belo-horizonte-e-regiao/autos-e-pecas/motos?o="+str(paginacao)+"&pe=8000&ps=2000&re=36&rs=28&sf=1"


opt_qtd_pag = int(input('Qts pág.? '))
qtd_pag = opt_qtd_pag + 1

# Inicia o browser
inicio = time.time()
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

chrome = webdriver.Chrome(desired_capabilities=capa)
wait = WebDriverWait(chrome, 20)


# Percorre a paginação da categoria para obter os links de todos os anúncios
url_list = []
falha_cap_pag = []

for i in (range(1, qtd_pag)):
    try:
        chrome.get(getUrl(i))
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-12rk7z2-0')))
        chrome.execute_script("window.stop();")
        
        itens = chrome.find_elements(by=By.CLASS_NAME, value="sc-12rk7z2-0")

        for item in itens:
            item_link = item.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
            url_list.append(item_link)
        print(f'Peguei a pág. {i} na 1ª tentativa')
    except:
        try:
            chrome.get(getUrl(i))
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-12rk7z2-0')))
            chrome.execute_script("window.stop();")
            
            itens = chrome.find_elements(by=By.CLASS_NAME, value="sc-12rk7z2-0")
        
            for item in itens:
                item_link = item.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
                url_list.append(item_link)
            print(f'Peguei a pág. {i} na 2ª tentativa')
        
        except:
            print(f' >>>>> Página -{i}- falhou!!!')
            falha_cap_pag.append(i)
            pass


print('#' * 100)
print()
print(f'>>>> {len(url_list)} Links encontrados')
print()
print('#' * 100)


print(f'Página(s) - {falha_cap_pag} - falhou(ram) na captura dos links.')


dados_anuncios = []



#Coleta dados de cada anuncio

contador = 0
cont_falha_captura = 0
for i, url in enumerate(url_list):
    contador += 1
    na = 1
    cont_while = 0
    while na == 1:
        cont_while += 1    
        try:
            recebe = pegaDados(chrome, url)
            atrib_anun = recebe[1]
            na = recebe[0]
            dados_anuncios.append(atrib_anun)
            print('Coletado')
                
        except:
            cont_falha_captura += 1
            print(f'Falha na captura: {cont_falha_captura} --- url: {url}')
            pass
        
        if cont_while == 10:
            break

    print(F'>>>>>>>>>>> NA: {na}')    
    print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Anuncios percorridos: {contador}')





data_e_hora_atuais = datetime.now()
data_atual = data_e_hora_atuais.strftime(r"%d_%m_%Y")
hora_atual = data_e_hora_atuais.strftime('%H_%M') 
var_data = f'{data_atual}___{hora_atual}.csv'
print(var_data)

# Salva os dados coletados em um arquivo csv
header = ['data','nome', 'preco', 'ano', 'km', 'cilindradas', 'marca','tipo', 'cidade', 'cod', 'url']
try:
    with open(var_data, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for elem in dados_anuncios:
            writer.writerow(elem)
    print('>>>> ARQUIVO .csv CRIADO COM SUCESSO! <<<')
except IOError:
    print("I/O error")

print('=' *100)
print(f'{"FINALIZADO":^100}')
print('=' *100)

print(f'Página(s) - {falha_cap_pag} - falhou(ram) na captura dos links.')
print(f'{contador} anuncio(s) foram percorridos.')
print(f'{cont_falha_captura} anuncio(s) falhou(ram) na captura dos dados.')
print(f'>>>>>>>>>>>>>>>> {contador - cont_falha_captura} ANUNCIOS CAPTURADOS!!!')

chrome.quit()

fim = time.time()
tempo_decorrido_minutos = (fim - inicio)/60
print(F' >>>>>>>>>>>  TEMPO DE EXECUÇÃO: {tempo_decorrido_minutos}')