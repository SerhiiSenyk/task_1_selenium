from source.pages.locators.locators import CategoryPageLocators
from source.pages.base import Base

class CategoryPage(Base):

    def goto_product(self):
        return self.goto_next_page(CategoryPageLocators.FIND_PRODUCT)
