from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from source.driver.factory import DriverFactory
from source.driver.driver_type import DriverType
from source.utils.singleton import singleton

@singleton
class Driver(WebDriver):

    def __init__(self, browser = DriverType.CHROME):
        self.driver = DriverFactory().get_driver(browser)
        self.driver.maximize_window()

    def __getattr__(self, item):
        return getattr(self.driver, item) 

