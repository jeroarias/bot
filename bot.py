#librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\drive'

driver = webdriver.Chrome()


#Inicializamos el navegador
driver.get('https://www.discord.com/')
#login de discord
element = driver.find_element(By.CSS_SELECTOR,'a.button-ZGMevK.buttonWhite-1M-wED.buttonSmall-1FIG7u.gtm-click-class-login-button.button-1I7cbj')
element.click()
element = driver.find_element(By.CSS_SELECTOR,'input#uid_5')
element.click()
element.send_keys('jeroariasm@gmail.com')
element = driver.find_element(By.CSS_SELECTOR,'input#uid_7')
element.click()
element.send_keys('dicardi7')
element = driver.find_element(By.CSSSELECTOR,'button.marginBottom8-emkd0.button-1cRKG6.button-ejjZWC.lookFilled-1H2Jvj.colorBrand-2M3O3N.sizeLarge-2xP3-w.fullWidth-3M-YBR.grow-2T4nbg')
element.click()


time.sleep(150)