
from selenium import webdriver
import time
class Bot:
    def __init__(self,usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        print('abrindo a pagina')
        self.driver.get('https://www.instagram.com/')
        self.driver.maximize_window()
        print('Pagina aberta')
    
    def logar(self):
        user = self.usuario
        key = self.senha
        time.sleep(5)
        print('inserindo usuario...')
        self.driver.find_element_by_name('username').send_keys(user) 
        print('usuario inserido')  
        time.sleep(3)
        print('inserindo senha...')
        self.driver.find_element_by_name('password').send_keys(key)
        print('senha inserida')
        print('entrando...')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]').click()
        print('conta logada')
        time.sleep(5)
    def seguir(self,hashtag):
        time.sleep(3)
        print('pesquisando hashtag')
        self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
        print('sucesso')
        time.sleep(4)
        for a in range(1,5):
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        hrefs = self.driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        seguidos = 0
        print('seguindo contas...')
        for pic_href in pic_hrefs:
            self.driver.get(pic_href)
            self.driver.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF     "]').click()
            time.sleep(5)
            print(f'seguindo: {seguidos+1}')
            seguidos += 1 
def main():
    user = input('digite seu usuario ou email: ')
    senha = input('digite sua senha: ')
    hashtag = input('digite a hashtag: #')
    teste = Bot(user,senha)
    teste.logar()
    teste.seguir(hashtag)
    
if __name__ == '__main__':
    main()

        
