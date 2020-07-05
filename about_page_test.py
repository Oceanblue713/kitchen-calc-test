from selenium import webdriver
from home_locators import HomePage, Buttons
import time

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(414, 736)
driver.get("https://www.yourkitchenapp.com")
time.sleep(1)
about_link = driver.find_element(*HomePage.about_link)
about_link.click()
time.sleep(2)
home_button = driver.find_element(*Buttons.home_button)
home_button.click()
time.sleep(1)

driver.quit()
print("About page test is done")
