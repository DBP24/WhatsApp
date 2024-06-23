from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
import base64
import time


class WhatsApp:

    def __init__(self) :
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920x1080')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
        
        self.driver = webdriver.Chrome(options=options)
        self.first_message = True
    
    def extraer_codigo_qr(self):
        self.driver.get('https://web.whatsapp.com/')

        qr_element = WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located((By.TAG_NAME,'canvas'))
            )
        
        qr_canvas = self.driver.find_element(By.TAG_NAME,'canvas')
        qr_base_64 = self.driver.execute_script("return arguments[0].toDataURL('image.png').substring(22);",qr_canvas)
        qr_file_path = 'code_whatsapp.png'
        with open(qr_file_path,'wb') as qr_file:
            qr_file.write(base64.b64decode(qr_base_64))
    
    def enviar_mensaje(self,contacto,msg):
        if self.first_message:
            self.first_message = False
            time.sleep(10)
        search_box = WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located((By.XPATH,"//div[@contenteditable='true'][@data-tab='3']"))
        )
        search_box.clear()
        search_box.send_keys(contacto)
        search_box.send_keys(u'\ue007')
        
        contacto = WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located((By.XPATH,f"//span[@title='Yo']"))
        )

        contacto.click()

        message_box = WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located((By.XPATH,"//div[@contenteditable='true'][@data-tab='10']"))
        )
        message_box.send_keys(msg)
        message_box.send_keys(u'\ue007')


if __name__ == '__main__':
    whatsapp = WhatsApp()
    whatsapp.extraer_codigo_qr()
   