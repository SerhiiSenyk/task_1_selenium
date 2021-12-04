from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator))

    def goto_site(self, url, time=15):
        self.driver.implicitly_wait(time)
        return self.driver.get(url)

    def goto_next_page(self, locator):
        try:
            self.element = self.find_element(locator)
            self.element.click()
            print('Click')
        except:
            print('Element not found or element not is button') 
        return self.element 
