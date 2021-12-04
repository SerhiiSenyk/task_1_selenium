from source.pages.base import Base
from source.pages.locators.locators import MainPageLocators

class MainPage(Base):      

    def load_page(self, url):
        res = True
        try:
            self.goto_site(url)
            print('Success load site')
        except:
            print('Error load site')
            res = False
        return res

    def goto_category(self):
        return self.goto_next_page(MainPageLocators.CATEGORY)
    

        