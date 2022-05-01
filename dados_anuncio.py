def pegaDados(url):

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
    
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    chrome = webdriver.Chrome(desired_capabilities=capa)
    wait = WebDriverWait(chrome, 20)

    chrome.get(url)

    wait.until(EC.presence_of_element_located((By.ID, 'initial-data')))

    chrome.execute_script("window.stop();")


    json_iten = chrome.find_element(by=By.ID, value="initial-data")
    atrib_json = json_iten.get_attribute('data-json')
    saida = html.escape(atrib_json)
    conv = html.unescape(saida)
    anuncio = json.loads(conv)

    try:
        data_anun = chrome.find_element(By.XPATH, '//body/div[2]/div/div[4]/div[2]/div/div[2]/div/div[27]/div/div/div/span[1]').get_attribute('innerHTML')
        dados['data'] = data_anun.split('em')[1].split('às')[0].split('>')[1]
    except:
        dados['data'] = 'N/A'

    try:
        nome = chrome.find_element(by=By.XPATH, value = "//head/title").get_attribute('innerHTML')
        dados['nome'] = nome.split('-')[0].strip()
        dados['cod'] = nome.split('-')[1].split('|')[0].strip()
    except:
        dados['nome'] = 'N/A'

    try:
        preco_anterior = anuncio['ad']["oldPrice"]
        dados['preco_anterior'] = preco_anterior
    except:
        dados['preco_anterior'] = 'N/A'

    try:
        preco_str = chrome.find_element(by=By.XPATH, value = "//body/div/div/div[4]/div/div/div[2]/div/div[12]/div/div/div/div/div/div/h2").get_attribute('innerHTML')
        numeros = ''
        for caractere in preco_str:
            if caractere.isdigit():
                numeros += caractere
        preco = int(numeros)
        dados['preco'] = preco
    except:
        dados['preco'] = 'N/A'

    try:
        imagem = anuncio['ad']["images"][0]["original"]
        dados['imagem'] = imagem
    except:
        dados['imagem'] = 'N/A'

    try:
        ano = chrome.find_element(by=By.XPATH, value = "//body/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/a").get_attribute('innerHTML')
        dados['ano'] = ano
    except:
        dados['ano'] = 'N/A'

    try:
        km = chrome.find_element(by=By.XPATH, value = "//body/div/div/div/div/div/div/div/div[22]/div/div/div/div/div[4]/div/dd").get_attribute('innerHTML')
        dados['km'] = km
    except:
        dados['km'] = 'N/A'

    try:
        cilindradas = anuncio['ad']["properties"][4]["value"]
        dados['cilindradas'] = cilindradas
    except:
        dados['cilindradas'] = 'N/A'

    try:    
        tipo = anuncio['ad']["trackingSpecificData"][1]["value"]
        dados['tipo'] = tipo
    except:
        dados['tipo'] = 'N/A'

    try:     
        cidade = chrome.find_element(By.XPATH, '//body/div/div/div/div/div/div/div/div[26]/div/div/div/div/div/div[2]/div/dd').get_attribute('innerHTML')
        dados['cidade'] = cidade
    except:
        dados['cidade'] = 'N/A'

    try:     
        bairro = chrome.find_element(By.XPATH, '//body/div/div/div/div/div/div/div/div[26]/div/div/div/div/div/div[3]/div/dd').get_attribute('innerHTML')
        dados['bairro'] = bairro
    except:
        dados['bairro'] = 'N/A'

    try:    
        cep = chrome.find_element(By.XPATH, '//body/div/div/div/div/div/div/div/div[26]/div/div/div/div/div/div[1]/div/dd').get_attribute('innerHTML')
        dados['cep'] = cep
    except:
        dados['cep'] = 'N/A'

    dados['url'] = url

    chrome.quit()

    fim = time.time()
    fim2 = fim - inicio
    print(f'>>>>>>>>>>>>>>>>>>>>>TEMPO: {fim2}')
    
    return dados

