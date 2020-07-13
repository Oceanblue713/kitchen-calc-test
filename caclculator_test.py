from selenium import webdriver
from home_locators import *
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
ozInput.send_keys(1)
time.sleep(1)

IbHeader = driver.find_element(*CalculatorPage.IbHeader)
print(IbHeader.text)
time.sleep
IbInput = driver.find_element(*CalculatorPage.IbInput)
IbInput.send_keys(1)
time.sleep(1)

TbHeader = driver.find_element(*CalculatorPage.TbHeader)
print(TbHeader.text)
time.sleep(2)
TbInput = driver.find_element(*CalculatorPage.TbInput)
TbInput.send_keys(1)
time.sleep(1)

CHeader = driver.find_element(*CalculatorPage.CHeader)
print(CHeader.text)
time.sleep(2)
CInput = driver.find_element(*CalculatorPage.CInput)
CInput.send_keys(1)
time.sleep(1)

InHeader = driver.find_element(*CalculatorPage.InHeader)
print(InHeader.text)
time.sleep(2)
InInput = driver.find_element(*CalculatorPage.InInput)
InInput.send_keys(1)
time.sleep(1)

feetHeader = driver.find_element(*CalculatorPage.feetHeader)
print(feetHeader.text)
time.sleep(2)
feetInput = driver.find_element(*CalculatorPage.feetInput)
feetInput.send_keys(1)
time.sleep(1)

mileHeader = driver.find_element(*CalculatorPage.mileHeader)
print(mileHeader.text)
time.sleep(2)
mileInput = driver.find_element(*CalculatorPage.mileInput)
mileInput.send_keys(1)
time.sleep(1)

home_button = driver.find_element(*Buttons.home_button)
home_button.click()
time.sleep(2)

print("Calculator test is done.")
driver.quit()
