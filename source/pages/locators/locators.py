from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_LIST = (By.ID, "result")
    GOTO_LIST = (By.XPATH, "html/body/div/div/div[2]/a")

class ListPageLocators:
    PHONE_NUMBER_FIELD = (By.NAME, 'phone')
    ORDER_BUTTON = (By.ID, 'result')

class MainPageLocators:
    CATEGORY = (By.LINK_TEXT , 'Новинки магазину')

class CategoryPageLocators:
    FIND_PRODUCT = (By.XPATH, '/html/body/div/center/div[3]/center/div/a[2]')