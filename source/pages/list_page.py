from source.pages.base import Base
from source.pages.locators.locators import ListPageLocators

class ListPage(Base):

    def add_phone_number(self):
        try:
            self.element = self.find_element(ListPageLocators.PHONE_NUMBER_FIELD)
            self.element.click()
            self.element.send_keys('000000000')
        except:
            print('Error add_phone_number')
        return self.element

    def to_order(self):
        return self.goto_next_page(ListPageLocators.ORDER_BUTTON)