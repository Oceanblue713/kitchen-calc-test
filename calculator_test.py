from selenium import webdriver
from home_locators import *
import time
import unittest


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.set_window_size(414, 736)
        self.addCleanup(self.driver.quit)

    def test_calculators(self):
        self.driver.get("https://www.yourkitchenapp.com")
        time.sleep(2)
        self.calc_link = self.driver.find_element(*HomePage.calc_link)
        self.calc_link.click()

        self.ozHeader = self.driver.find_element(*CalculatorPage.ozHeader)
        print(self.ozHeader.text)
        time.sleep(2)
        self.ozInput = self.driver.find_element(*CalculatorPage.ozInput)
        self.ozInput.send_keys(1)
        time.sleep(1)

        self.IbHeader = self.driver.find_element(*CalculatorPage.IbHeader)
        print(self.IbHeader.text)
        time.sleep(2)
        self.IbInput = self.driver.find_element(*CalculatorPage.IbInput)
        self.IbInput.send_keys(1)
        time.sleep(1)

        self.TbHeader = self.driver.find_element(*CalculatorPage.TbHeader)
        print(self.TbHeader.text)
        time.sleep(2)
        self.TbInput = self.driver.find_element(*CalculatorPage.TbInput)
        self.TbInput.send_keys(1)
        time.sleep(1)

        self.CHeader = self.driver.find_element(*CalculatorPage.CHeader)
        print(self.CHeader.text)
        time.sleep(2)
        self.CInput = self.driver.find_element(*CalculatorPage.CInput)
        self.CInput.send_keys(1)
        time.sleep(1)

        self.IbHeader = self.driver.find_element(*CalculatorPage.IbHeader)
        print(self.IbHeader.text)
        time.sleep(2)
        self.IbInput = self.driver.find_element(*CalculatorPage.IbInput)
        self.IbInput.send_keys(1)
        time.sleep(2)

        self.feetHeader = self.driver.find_element(*CalculatorPage.feetHeader)
        print(self.feetHeader.text)
        time.sleep(2)
        self.feetInput = self.driver.find_element(*CalculatorPage.feetInput)
        self.feetInput.send_keys(1)
        time.sleep(1)

        self.mileHeader = self.driver.find_element(*CalculatorPage.mileHeader)
        print(self.mileHeader.text)
        time.sleep(2)
        self.mileInput = self.driver.find_element(*CalculatorPage.mileInput)
        self.mileInput.send_keys(1)
        time.sleep(1)

        self.home_button = self.driver.find_element(*Buttons.home_button)
        self.home_button.click()
        time.sleep(2)

        print("Calculator test is done.")


if __name__ == "__main__":
    unittest.main(verbosity=1)