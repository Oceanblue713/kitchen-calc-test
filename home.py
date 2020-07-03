from selenium import webdriver
from Locators import HomePage, CalculatorPage
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.yourkitchenapp.com/')
print(driver.title)

Logo = driver.find_element(*HomePage.logo)
Logo.click()
time.sleep()

about_link = driver.find_element(*HomePage.about_link)
about_link.click()
time.sleep(2)

driver.get('https://www.yourkitchenapp.com/')
calc_link = driver.find_element(*HomePage.calc_link)
calc_link.click()

ozHeader = driver.find_element(*CalculatorPage.ozHeader)
print(ozHeader.text)
time.sleep(2)
ozInput = driver.find_element(*CalculatorPage.ozInput)
ozInput.send_keys("1")
time.sleep(2)

driver.quit()