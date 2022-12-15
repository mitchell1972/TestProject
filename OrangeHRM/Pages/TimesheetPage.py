from selenium.webdriver.common.by import By

from OrangeHRM.Pages.LoginPage import LoginPage


class TimesheetPage:
    timesheet_page = LoginPage()

    def employee_name(self):
        self.timesheet_page.return_called_driver().find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div["
                                                                          "1]/form/div[1]/div/div/div/div["
                                                                          "2]/div/div/input").send_keys("Paul Collings")

    def view_button(self):
        self.timesheet_page.return_called_driver().find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div["
                                                                          "2]/div/div[1]/form/div[2]/button").click()
