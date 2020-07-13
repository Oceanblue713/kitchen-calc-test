from selenium import webdriver
from home_locators import *
import time

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(414, 736)
driver.get("https://www.yourkitchenapp.com/")
watch_link = driver.find_element(*HomePage.watch_link)
watch_link.click()
time.sleep(2)

start_button = driver.find_element(*WatchPage.start_button)
start_button.click()
print("Start watch")
time.sleep(5)
stop_button = driver.find_element(*WatchPage.stop_button)
stop_button.click()
print("Stop watch")
time.sleep(2)
reset_button = driver.find_element(*WatchPage.reset_button)
reset_button.click()
print("Reset watch")
time.sleep(2)

home_button = driver.find_element(*Buttons.home_button)
home_button.click()
time.sleep(1)

print("Watch test is done")
driver.quit()

