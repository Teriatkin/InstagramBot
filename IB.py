from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
        #Відкриття браузера
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        #Закриття браузера
    def closeBrowser(self):
        self.driver.close()
        #Вхід в інстаграм
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        #Підписки
    def subscribe(self, follower):
        driver = self.driver
        driver.get("https://www.instagram.com/" + follower + "/")
        time.sleep(2)
        subscribe = driver.find_elements_by_xpath("//*[contains(text(), 'Подписаться')]")
        for i in subscribe:
            i.click()
        time.sleep(2)



