from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
#        self.base_url = "https://www.google.com/"
#        self.verificationErrors = []
#        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
