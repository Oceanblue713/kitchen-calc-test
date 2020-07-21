from selenium import webdriver
from home_locators import *
import time
import unittest


class HomePageTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.set_window_size(414, 736)
        self.addCleanup(self.browser.quit)

    def test_aboutPage(self):
        self.browser.get('https://www.yourkitchenapp.com/')
        print(self.browser.title)
        self.about_link = self.browser.find_element(*HomePage.about_link)
        self.about_link.click()
        time.sleep(2)

    def test_calcPage(self):
        self.browser.get('https://www.yourkitchenapp.com/')
        time.sleep(1)
        calc_link = self.browser.find_element(*HomePage.calc_link)
        calc_link.click()
        time.sleep(2)

    def test_watchPage(self):
        self.browser.get('https://www.yourkitchenapp.com/')
        time.sleep(1)
        watch_link = self.browser.find_element(*HomePage.watch_link)
        watch_link.click()
        time.sleep(2)

    def test_shortreadsPage(self):
        self.browser.get('https://www.yourkitchenapp.com/')
        time.sleep(1)
        short_reads_link = self.browser.find_element(*HomePage.short_reads_link)
        short_reads_link.click()
        time.sleep(2)


print("Home Page Test is done")

if __name__ == '__main__':
    unittest.main(verbosity=1)
