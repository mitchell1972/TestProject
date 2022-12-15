
from jproperties import Properties
from OrangeHRM.Utils.Utilities import Utility


class Drivers:
    configs = Properties()
    browser = ""
    util = Utility()

    # def __init__(self):
    #     self.util.get_config_browser()

    def setup(self):
        return self.browser

    def select_browser(self):
        return self.util.get_config_browser()
