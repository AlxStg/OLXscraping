from time import sleep


def pegaDados(chrome, url):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import json
    import html
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.support import expected_conditions as EC
    import time

    inicio = time.time()

    
    dados = {}
    
 
    wait = WebDriverWait(chrome, 20)

    chrome.get(url)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hb5mou-0")))
    # sleep(2)
    chrome.execute_script("window.stop();")


    json_iten = chrome.find_element(by=By.ID, value="initial-data")
    atrib_json = json_iten.get_attribute('data-json')
    saida = html.escape(atrib_json)
    conv = html.unescape(saida)
    anuncio = json.loads(conv)

    na = 0


    try:
        data_anun = chrome.find_element(By.XPATH, '//body/div[2]/div/div[4]/div[2]/div/div[2]/div/div[27]/div/div/div/span[1]').get_attribute('innerHTML')
        dados['data'] = data_anun.split('em')[1].split('às')[0].split('>')[1]
    except:
        na = 1
        dados['data'] = 'N/A'

    try:
        nome = chrome.find_element(by=By.XPATH, value="//head/title").get_attribute('innerHTML')
        dados['nome'] = nome.split('-')[0].strip()
    except:
        na = 1
        dados['nome'] = 'N/A'

    try:
        marca = chrome.find_element(by=By.XPATH, value="//head/title").get_attribute('innerHTML')
        dados['marca'] = marca.split(' ')[0].strip()
        print(dados['marca'])
    except:
        na = 1
        dados['marca'] = 'N/A'

    try:
        codigo = chrome.find_element(by=By.CLASS_NAME, value="sc-16iz3i7-0").get_attribute('innerHTML')
        dados['cod'] = codigo.split('>')[1]
    except:
        na = 1
        dados['cod'] = 'N/A'

    try:
        preco_str = chrome.find_element(by=By.XPATH, value = "//body/div/div/div/div/div/div/div/div/div/div/div/div[2]/h2[2]").get_attribute('innerHTML')
        numeros = ''
        for caractere in preco_str:
            if caractere.isdigit():
                numeros += caractere
        preco = int(numeros)
        dados['preco'] = preco
    except:
        na = 1
        dados['preco'] = 'N/A'            

    try:
        ano = chrome.find_element(by=By.XPATH, value = "//body/div/div/div/div/div/div/div/div[22]/div/div/div/div/div[3]/div/a").get_attribute('innerHTML')
        dados['ano'] = ano
    except:
        nome_an = nome.split('-')[0].strip()[-4::]
        if nome_an.isdigit():
            dados['ano'] = nome_an
        else:
            na = 1
            dados['ano'] = 'N/A'

    try:
        km = chrome.find_element(by=By.XPATH, value = "//body/div/div/div/div/div/div/div/div[22]/div/div/div/div/div[4]/div/dd").get_attribute('innerHTML')
        dados['km'] = km
    except:
        dados['km'] = None

    try:
        cilindradas = anuncio['ad']["properties"][4]["value"]
        dados['cilindradas'] = cilindradas
    except:
        dados['cilindradas'] = None

    try:    
        tipo = anuncio['ad']["trackingSpecificData"][1]["value"]
        dados['tipo'] = tipo
    except:
        nome_tip = nome.split(' ')[1].split(' ')[0]
        dados['tipo'] = nome_tip

    try:     
        cidade = chrome.find_element(By.XPATH, '//body/div/div/div/div/div/div/div/div[26]/div/div/div/div/div/div[2]/div/dd').get_attribute('innerHTML')
        dados['cidade'] = cidade
    except:
        dados['cidade'] = None

    dados['url'] = url

    saida = [na , dados]

    fim = time.time()
    fim2 = fim - inicio
    print(f'>>>>>>>>>>>>>>>>>>>>>TEMPO: {fim2}')
    
   
    return saida
    
