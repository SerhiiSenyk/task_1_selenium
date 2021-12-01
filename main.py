from selenium import webdriver
import time

url = 'https://man7.org/linux/man-pages/man2/socket.2.html'
delay = 3

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(delay)
try:
	element = driver.find_element_by_link_text('accept(2)')
	time.sleep(delay)
except:
	print('Failed')
else:
	element.click()
	time.sleep(delay)