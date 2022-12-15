from selenium.webdriver.common.by import By

from OrangeHRM.Pages.LoginPage import LoginPage
from OrangeHRM.Pages.TimesheetPage import TimesheetPage
from OrangeHRM.Pages.DashboardLeftMenu import DashboardLeft


class ClickTimeMenu:

    @staticmethod
    def select_time_menu():
        login_page = LoginPage()
        dashboard = DashboardLeft()
        timesheet = TimesheetPage()
        dashboard.time_menu()
        assert login_page.return_called_driver().current_url == "https://opensource-demo.orangehrmlive.com/web/index" \
                                                                ".php/time/viewEmployeeTimesheet"
        timesheet.employee_name()
        timesheet.view_button()
        # Assert that the time sheet for the employee entered is displayed
        assert login_page.return_called_driver().current_url == "https://opensource-demo.orangehrmlive.com/web/index" \
                                                                ".php/time/viewTimesheet/employeeId/5 "


