from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from jproperties import Properties
import os


class Utility:
    configs = Properties()
    browser = ""
    driver = webdriver.Chrome()
    username = ""
    password = ""

    def setup_app_config(self):
        dir_path = os.path.dirname(os.path.realpath('../../app-config.properties'))
        with open(dir_path + '/app-config.properties', 'rb') as config_file:
            self.configs.load(config_file)
        return self.configs

    def get_config_browser(self):
        self.browser = self.setup_app_config().get("browser").data
        if self.browser.lower() == "chrome":
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.implicitly_wait(15)
        elif self.browser.lower() == "firefox":
            self.driver = webdriver.Firefox(GeckoDriverManager().install())
        return self.driver

    def get_username_and_password(self):
        username = self.setup_app_config().get("username").data
        password = self.setup_app_config().get("password").data
        username_password = (username, password)
        return username_password

    def return_called_driver(self):
        return self.driver
