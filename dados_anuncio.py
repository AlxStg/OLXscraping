def pegaDados(url):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import json
    import html
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.support import expected_conditions as EC

    url_a = str(url)
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
    chrome.quit()

    anuncio = json.loads(conv)
    try:
        nome = anuncio['ad']["properties"][1]["value"]
        dados['nome'] = nome
    except:
        dados['nome'] = 'N/A'

    try:
        preco_anterior = anuncio['ad']["oldPrice"]
        dados['preco_anterior'] = preco_anterior
    except:
        dados['preco_anterior'] = 'N/A'

    try:
        preco_str = anuncio['ad']["priceValue"]
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
        ano = anuncio['ad']["properties"][2]["value"]
        dados['ano'] = ano
    except:
        dados['ano'] = 'N/A'

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
        cidade = anuncio['ad']["location"]["municipality"]
        dados['cidade'] = cidade
    except:
        dados['cidade'] = 'N/A'

    try:    
        cep = anuncio['ad']["location"]["zipcode"]
        dados['cep'] = cep
    except:
        dados['cep'] = 'N/A'

    dados['url_anuncio'] = url_a

    print('>>>>>>>>> DICIONÁRIO <<<<<<<<<')
    print(dados)
    
    return dados

