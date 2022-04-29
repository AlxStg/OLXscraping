def pegaDados(url):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import json
    import html
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.support import expected_conditions as EC


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

    nome = anuncio['ad']["properties"][1]["value"]
    dados['nome'] = nome

    preco_anterior = anuncio['ad']["oldPrice"]
    dados['preco_anterior'] = preco_anterior

    preco_str = anuncio['ad']["priceValue"]
    numeros = ''
    for caractere in preco_str:
        if caractere.isdigit():
            numeros += caractere
    preco = int(numeros)
    dados['preco'] = preco

    imagem = anuncio['ad']["images"][0]["original"]
    dados['imagem'] = imagem

    ano = anuncio['ad']["properties"][2]["value"]
    dados['ano'] = ano

    cilindradas = anuncio['ad']["properties"][4]["value"]
    dados['cilindradas'] = cilindradas

    tipo = anuncio['ad']["trackingSpecificData"][1]["value"]
    dados['tipo'] = tipo

    cidade = anuncio['ad']["location"]["municipality"]
    dados['cidade'] = cidade

    cep = anuncio['ad']["location"]["zipcode"]
    dados['cep'] = cep
    dados['url_anuncio'] = url
    print('>>>>>>>>> DICIONÁRIO <<<<<<<<<')
    print(dados)
    print('>>>>>>>>> SAÍDA <<<<<<<<<')
    print(f'''NOME: {nome}
    CILINDRADA: {cilindradas} 
    PREÇO: R${preco:.2f} 
    PREÇO ANTERIOR: {preco_anterior}
    IMG. URL: {imagem} 
    ANO DE FABRICAÇÃO: {ano}
    CC: {cilindradas}
    Tipo: {tipo}
    Anuncio = {url}


        ''')
    return dados

