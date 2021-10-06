from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import json


def disparar_mensagem(mensagem):
    driver = webdriver.Chrome(executable_path='envio_mensagem_whatsapp/chromedriver.exe')
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 20)

    # Alteração para desmarcar a flag de manter conectado
    remember_me = driver.find_element_by_name("rememberMe")
    remember_me.click()

    # abre os contatos armazenados em json
    with open('envio_mensagem_whatsapp/contatos/contatos.json', "r") as data:
        contatos = json.load(data)

    # Busca pelo search de contatos
    search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    person_title = wait.until(lambda driver: driver.find_element_by_xpath(search_box))

    # Limpa a caixa de busca se estiver preenchida
    person_title.clear()

    # Iterate excel rows till to finish
    for contato in contatos['Nome']:
        # busca pelo contato
        person_title.send_keys(contatos['Nome'][str(contato)])

        # Wait for 3 seconds to search contact number
        time.sleep(3)

        try:
            # Load error message in case unavailability of contact number
            element = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span')
        except NoSuchElementException:
            person_title.send_keys(Keys.ENTER)
            mensagem_cortada = mensagem.split('\n')
            input_texto = driver.find_element_by_xpath("//div[contains(., 'Digite uma mensagem')]/following-sibling::div")
            for linha in mensagem_cortada:
                if linha == '':
                    input_texto.send_keys(Keys.SHIFT, '\n')
                else:
                    input_texto.send_keys(linha)
                    input_texto.send_keys(Keys.SHIFT, '\n')
            input_texto.send_keys(Keys.ENTER)

    # Close Chrome browser
    driver.quit()