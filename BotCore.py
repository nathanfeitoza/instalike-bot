from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

class BotCore:
    def __init__(self):
        self.__urlInstagram = "https://www.instagram.com/"
        self.__urlInstalike = "https://instelikes.com.br/app#login"
        self.__instalikeEmail = ""
        self.__instalikePass = ""
        self.__loginInstagram = ""
        self.__passInstagram = ""
        self.__browser = None
        self.__setBrowser()
    
    def setLoginInstagram(self, login, password):
        self.__loginInstagram = login
        self.__passInstagram = password

    def setLoginInstalike(self, email, password):
        self.__instalikeEmail = email
        self.__instalikePass = password

    def __reset(self):
        self.__browser = None
        self.__setBrowser()
    
    def __loginInstalike(self):
        self.__browser.get(self.__urlInstalike)
        time.sleep(3)
        self.__browser.find_element_by_xpath('/html/body/main/x-active-template/div/div/div/div/div/div/form/x-default-template/div/div[1]/input').send_keys(self.__instalikeEmail)
        print("Email instalike Inserido")
        self.__browser.find_element_by_id('login-step1').click()
        print("Próximo Passo login Instalike")
        time.sleep(2)
        self.__browser.find_element_by_xpath('/html/body/main/x-active-template/div/div/div/div/div/div/form/x-active-template/div/div[1]/input').send_keys(self.__instalikePass)
        print("Senha Inserida Instalike")
        self.__browser.find_element_by_id('login-submit').click()
        time.sleep(3)
        print('Login Instalike realizado')
    
    def __logarInstagram(self):
        print("Logando Instagram")
        self.__browser.get(self.__urlInstagram)
        time.sleep(3)
        self.__browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(self.__loginInstagram)
        self.__browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(self.__passInstagram)
        self.__browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        print("Logado no instagram")
        time.sleep(2)

    def __setBrowser(self):
        try:
            caps = DesiredCapabilities().CHROME.copy()
            caps["pageLoadStrategy"] = "eager"
            self.__browser = webdriver.Chrome(capabilities=caps)
        
        except:
            caps = DesiredCapabilities().FIREFOX.copy()
            caps["pageLoadStrategy"] = "eager"
            self.__browser = webdriver.Firefox(capabilities=caps)
    
    def __initProcessSeguirInstalike(self):
        print("Iniciado seleção de seguir")
        self.__browser.find_element_by_xpath("/html/body/aside[1]/div[2]/ul[1]/li[2]/a").click()
        time.sleep(3)
        self.__browser.find_element_by_xpath("/html/body/main/x-active-template/div/div/div[2]/form/div").click()
        print("Escolher a opção de seguir")
        time.sleep(1)
        self.__browser.find_element_by_xpath("/html/body/main/x-active-template/div/div/div[2]/form/div/div/div[3]/div/label[2]/input").click()
        print("Opção seguir ativada")
        self.__browser.find_element_by_xpath("/html/body/main/x-active-template/div/div/div[2]/form/button").click()
        print("Seguir iniciado")
        time.sleep(2)
        seguidos = 1

        while True:
            time.sleep(2)
            elements = self.__browser.find_elements_by_css_selector(".column.is-3-fullhd.is-4-desktop.is-6-tablet.is-12-mobile.request-box")
            if len(elements) == 0:
               self.__browser.close()
               time.sleep(3)
               self.__reset()
               self.initBot()
               break

            count = 0

            for element in elements:
                element.find_elements_by_css_selector("button.is-md.solid-button.is-bold")[0].click()
                time.sleep(3)
                self.__browser.switch_to.window(self.__browser.window_handles[1])
                time.sleep(4)
                
                self.__browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/button").click()
                self.__browser.close()
                self.__browser.switch_to.window(self.__browser.window_handles[0])
                time.sleep(3)
                self.__browser.find_element_by_xpath("/html/body/main/x-active-template/dialog[1]/div[2]/div/div[2]/form/button[2]").click()
                print("Seguidos: ", seguidos)
                seguidos += 1
                count += 1
                time.sleep(6)


    def initBot(self):
        self.__logarInstagram()
        self.__loginInstalike()
        self.__initProcessSeguirInstalike()