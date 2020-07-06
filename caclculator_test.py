from selenium import webdriver
from home_locators import HomePage ,CalculatorPage
import time

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(414, 736)
driver.get("https://www.yourkitchenapp.com")
time.sleep(2)
calc_link = driver.find_element(*HomePage.calc_link)
calc_link.click()

ozHeader = driver.find_element(*CalculatorPage.ozHeader)
print(ozHeader.text)
time.sleep(2)
ozInput = driver.find_element(*CalculatorPage.ozInput)
ozInput.send_keys("1")
time.sleep(2)

driver.quit()