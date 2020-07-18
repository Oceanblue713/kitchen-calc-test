from selenium import webdriver
from home_locators import *
import time
import unittest


class watchTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.set_window_size(414, 736)
        self.addCleanup(self.browser.quit)

    def test_watch(self):
        self.browser.get('https://www.yourkitchenapp.com/')
        self.watch_link = self.browser.find_element(*HomePage.watch_link)
        self.watch_link.click()
        time.sleep(2)

        self.start_button = self.browser.find_element(*WatchPage.start_button)
        self.start_button.click()
        print("Start watch")
        time.sleep(5)
        self.stop_button = self.browser.find_element(*WatchPage.stop_button)
        self.stop_button.click()
        print("Stop watch")
        time.sleep(2)
        self.reset_button = self.browser.find_element(*WatchPage.reset_button)
        self.reset_button.click()
        print("Reset watch")
        time.sleep(2)

        self.home_button = self.browser.find_element(*Buttons.home_button)
        self.home_button.click()
        time.sleep(1)

        print("Watch test is done")


if __name__ == '__main__':
    unittest.main(verbosity=1)