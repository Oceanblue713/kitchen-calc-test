from selenium import webdriver
from home_locators import *
import time
import unittest


class ShortReadsTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.set_window_size(414, 736)
        self.addCleanup(self.driver.quit)

    def test_short_reads(self):
        self.driver.get("https://www.yourkitchenapp.com/")
        time.sleep(1)
        self.short_reads_link = self.driver.find_element(*HomePage.short_reads_link)
        self.short_reads_link.click()

        self.article1 = self.driver.find_element(*ShortReadsPage.article1)
        self.article1.click()
        self.header1 = self.driver.find_element(*ShortReadsPage.header)
        print(self.header1.text)
        time.sleep(2)
        self.reads_button = self.driver.find_element(*Buttons.reads_button)
        self.reads_button.click()
        time.sleep(2)

        self.article2 = self.driver.find_element(*ShortReadsPage.article2)
        self.article2.click()
        self.header2 = self.driver.find_element(*ShortReadsPage.header)
        print(self.header2.text)
        time.sleep(2)
        self.reads_button = self.driver.find_element(*Buttons.reads_button)
        self.reads_button.click()
        time.sleep(2)

        self.article3 = self.driver.find_element(*ShortReadsPage.article3)
        self.article3.click()
        self.header3 = self.driver.find_element(*ShortReadsPage.header)
        print(self.header3.text)
        time.sleep(2)
        self.reads_button = self.driver.find_element(*Buttons.reads_button)
        self.reads_button.click()
        time.sleep(2)

        self.home_button = self.driver.find_element(*Buttons.home_button)
        self.home_button.click()
        time.sleep(2)

        print("The short reads test is done.")

if __name__ == "__main__":
    unittest.main(verbosity=1)