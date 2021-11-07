from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\karat\\OneDrive\\Desktop\\dev\\bryanu\\afs215\\week3\\driver\\chromedriver.exe')
driver.implicitly_wait(40)
driver.set_page_load_timeout(50)
driver.get("https://google.com")

search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("Sunapee New Hampshire")
search_bar.send_keys(Keys.RETURN)



