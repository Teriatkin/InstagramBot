from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    #конструктор __init__; відкриття браузера
    def __init__(self, username, password, *follower):
        self.username = username
        self.password = password
        self.follower = follower
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

    #Підписатися на акаунт
    def subscribe(self):
        driver = self.driver
        follower = self.follower
        for i in follower:
            driver.get("https://www.instagram.com/" + i + "/")
            time.sleep(2)
            subscribe = driver.find_elements_by_xpath("//*[contains(text(), 'Подписаться')]")
            subscribe[0].click()
            time.sleep(2)

    #Відписатися від всіх друзів
    def unsubscribe(self):
        driver = self.driver

        for i in range(95):
            driver.get("https://www.instagram.com/" + self.username + "/")
            subscribe = driver.find_elements_by_xpath("//*[contains(text(), 'Подписки:')]")
            subscribe[0].click()
            time.sleep(1)
            subscribe = driver.find_elements_by_xpath("//*[contains(text(), 'Подписки')]")
            subscribe[random.randint(1, 5)].click()
            time.sleep(random.randint(25, 30))
            confirm = driver.find_elements_by_xpath("//*[contains(text(), 'Отменить подписку')]")
            confirm[1].click()
            time.sleep(random.randint(1, 3))
