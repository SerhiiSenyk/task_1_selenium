from source.pages.base import Base
from source.pages.locators.locators import ProductPageLocators

class ProductPage(Base):

    def add_to_list(self):
        try:
            self.element = self.find_element(ProductPageLocators.ADD_TO_LIST)
            self.element.click()
        except:
            print('Failed add to list')
        return self.element

    def goto_list(self):
        return self.goto_next_page(ProductPageLocators.GOTO_LIST)