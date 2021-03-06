from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):  # закрываем браузер
        self.driver.quit()

    def is_valid(self): # проверяем валидность адреса
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):  # открываем главную страницу
        driver = self.driver
        driver.get("http://localhost/addressbook/")









