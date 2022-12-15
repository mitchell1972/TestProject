import time

from selenium.webdriver.common.by import By

from OrangeHRM.Utils.Driver import Drivers
from OrangeHRM.Utils.Utilities import Utility


class LoginPage:
    username = ""
    password = ""
    driver = Drivers()
    util = Utility()
    call_driver = driver.select_browser()

    def __init__(self, user_name=None, password=None):
        self.username = user_name
        self.password = password

    def return_called_driver(self):
        return self.call_driver

    def navigate_to_login_page(self):
        self.return_called_driver().get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.return_called_driver().maximize_window()

    def user_name(self, username):
        self.return_called_driver().find_element(By.NAME, "username").send_keys(username)

    def login_password(self, password):
        self.return_called_driver().find_element(By.NAME, "password").send_keys(password)

    def login_button(self):
        self.return_called_driver().find_element(By.XPATH,
                                                  "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
