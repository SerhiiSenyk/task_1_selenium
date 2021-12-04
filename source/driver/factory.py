from selenium import webdriver
from source.driver.driver_type import DriverType

class DriverFactory():

    @staticmethod
    def get_driver(driver_name = DriverType.CHROME):
        if driver_name == DriverType.CHROME:
            _single_web_driver = webdriver.Chrome()
        elif driver_name == DriverType.FIREFOX:
            _single_web_driver = webdriver.Firefox()
        elif driver_name == DriverType.EDGE:
            _single_web_driver = webdriver.Edge()
        else:
            raise ValueError('Unknown or unsupported name of browser')
        return _single_web_driver
