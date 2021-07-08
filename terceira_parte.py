# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:44:24 2021

@author: cartola
"""

"""
Funcionalidade: Tentar logar no site
Cenário: Logar no site com dados de login não cadastrados
Dado que navego para a página 'login' do site
E digito 'falsiane' no campo 'Username'
E digito '1234' no campo 'Password'
Quando clico no botão 'SIGN IN'
Então verifico se será exibida a mensagem de erro 'ERROR! Logging In Failed.'
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class Escuta(AbstractEventListener):
    
    """
    def before_click(self, elemento, webdriver):
        
        print(f'elemento: {elemento.tag_name}')
        sleep(1)
        
        if elemento.tag_name == 'div':
            wdw.until(esperar_mensagem, 'Mensagem não encontrada')
            print(f'elementoooo: {elemento.tag_name}')
            #sleep(3)
            #mensagem_de_erro = envolocro_browser.find_element_by_class_name('container').find_element_by_tag_name('div').text
            #mensagem_de_erro = envolocro_browser.find_elements_by_css_selector('.alert')[0].text
            #print(mensagem_de_erro)
            #assert mensagem_de_erro == 'ERROR! Logging In Failed.', 'Mensagem de erro não confere!'
            
    """
        
    def before_close(self, webdriver):
            mensagem_de_erro = envolocro_browser.find_element_by_class_name('container').find_element_by_tag_name('div').text
            print(f'mensagem de erro: {mensagem_de_erro}')
            assert mensagem_de_erro == 'ERROR! Logging In Failed.', 'Mensagem de erro não confere!'

def esperar_mensagem(webdriver):
    
    mensagem = envolocro_browser.find_elements_by_css_selector('.alert')
    print('Tentando encontrar..')
    return bool(mensagem)

url = 'https://opentdb.com/'

browser = Firefox()
envolocro_browser = EventFiringWebDriver(browser, Escuta())
wdw = WebDriverWait(envolocro_browser, 10)
envolocro_browser.get(url)
sleep(2)

lista_li = envolocro_browser.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
lista_li[-1].click()
sleep(2)

campo_username = envolocro_browser.find_element_by_id('username')
campo_password = envolocro_browser.find_element_by_id('password')

campo_username.send_keys('falsiane')
campo_password.send_keys('1234')

botao_sign_in = envolocro_browser.find_element_by_tag_name('form').find_elements_by_tag_name('div')[1]
botao_sign_in.click()
envolocro_browser.close()


