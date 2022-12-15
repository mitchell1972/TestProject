
from selenium.webdriver.common.by import By

from OrangeHRM.Pages.LoginPage import LoginPage
from OrangeHRM.Utils.Utilities import Utility


class Login:
    def __init__(self):
        pass

    @staticmethod
    def log_into_app():
        util = Utility()
        login = LoginPage(util.get_username_and_password()[0], util.get_username_and_password()[1])
        login.navigate_to_login_page()
        login.user_name(login.username)
        login.login_password(login.password)
        login.login_button()
        assert login.return_called_driver().current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        element = login.return_called_driver().find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]")
        assert element.text == "Dashboard"
