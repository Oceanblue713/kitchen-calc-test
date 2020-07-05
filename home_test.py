from selenium import webdriver
from home_locators import HomePage, CalculatorPage
import time

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(414, 736)
driver.get('https://www.yourkitchenapp.com/')
print(driver.title)

about_link = driver.find_element(*HomePage.about_link)
about_link.click()
time.sleep(2)

driver.get('https://www.yourkitchenapp.com/')
time.sleep(1)
calc_link = driver.find_element(*HomePage.calc_link)
calc_link.click()
time.sleep(2)

driver.get('https://www.yourkitchenapp.com/')
time.sleep(1)
watch_link = driver.find_element(*HomePage.watch_link)
watch_link.click()
time.sleep(2)

driver.get('https://www.yourkitchenapp.com/')
time.sleep(1)
short_reads_link = driver.find_element(*HomePage.short_reads_link)
short_reads_link.click()
time.sleep(2)

# ozHeader = driver.find_element(*CalculatorPage.ozHeader)
# print(ozHeader.text)
# time.sleep(2)
# ozInput = driver.find_element(*CalculatorPage.ozInput)
# ozInput.send_keys("1")
# time.sleep(2)

driver.quit()
print("Home Page Test is done")
