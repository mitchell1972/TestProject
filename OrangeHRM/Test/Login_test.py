from OrangeHRM.Steps.Login import Login
from OrangeHRM.Steps.ClickOnTimeMenu import ClickTimeMenu

login = Login()
menu = ClickTimeMenu()


def test_login():
    login.log_into_app()


def test_time_sheet():
    menu.select_time_menu()
