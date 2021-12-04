from source.pages.main_page import MainPage
from source.pages.category_page import CategoryPage
from source.pages.product_page import ProductPage
from source.pages.list_page import ListPage

url = 'https://hobbymania.com.ua'

def test_main_page(browser):
    main_page = MainPage(browser)
    assert main_page.load_page(url) == True
    assert not main_page.goto_category() == None
    
def test_category_page(browser):
    category_page = CategoryPage(browser)
    assert not category_page.goto_product() == None

def test_product_page(browser):
    product_page = ProductPage(browser)
    assert not product_page.add_to_list() == None
    assert not product_page.goto_list() == None

def test_list_page(browser):
    list_page = ListPage(browser)
    assert not list_page.add_phone_number() == None
    #list_page.to_order()