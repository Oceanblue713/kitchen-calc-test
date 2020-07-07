from selenium import webdriver
from home_locators import HomePage, ShortReadsPage, Buttons
import time

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(414, 736)
driver.get("https://www.yourkitchenapp.com/")
time.sleep(1)
short_reads_link = driver.find_element(*HomePage.short_reads_link)
short_reads_link.click()

article1 = driver.find_element(*ShortReadsPage.article1)
article1.click()
header1 = driver.find_element(*ShortReadsPage.header)
print(header1.text)
time.sleep(2)
reads_button = driver.find_element(*Buttons.reads_button)
reads_button.click()
time.sleep(2)

article2 = driver.find_element(*ShortReadsPage.article2)
article2.click()
header2 = driver.find_element(*ShortReadsPage.header)
print(header2)
time.sleep(2)
reads_button = driver.find_element(*Buttons.reads_button)
reads_button.click()
time.sleep(2)

article3 = driver.find_element(*ShortReadsPage.article3)
article3.click()
header3 = driver.find_element(*ShortReadsPage.header)
print(header3)
time.sleep(2)
reads_button = driver.find_element(*Buttons.reads_button)
reads_button.click()
time.sleep(2)

home_button = driver.find_element(*Buttons.home_button)
home_button.click()
time.sleep(2)

print("The short reads test is done.")
driver.quit()