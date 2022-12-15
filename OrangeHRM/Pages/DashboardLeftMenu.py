from selenium.webdriver.common.by import By
from OrangeHRM.Pages.LoginPage import LoginPage


class DashboardLeft:
    login_page = LoginPage()

    def time_menu(self):
        self.login_page.return_called_driver().find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div["
                                                                      "2]/ul/li[4]/a/span").click()
