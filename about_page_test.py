from selenium import webdriver
from home_locators import *
import time
import unittest


class AboutPageTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.set_window_size(414, 736)
        self.addCleanup(self.browser.quit)

    def test_aboutPage(self):
        self.browser.get("https://www.yourkitchenapp.com")
        time.sleep(1)
        about_link = self.browser.find_element(*HomePage.about_link)
        about_link.click()
        time.sleep(2)
        about_page_text = self.browser.find_element(*AboutPage.about_this_page)
        self.assertIn('About This Page', about_page_text.text)
        print (about_page_text.text)
        about_the_creator = self.browser.find_element(*AboutPage.about_the_creator)
        self.assertIn("About The Creator", about_the_creator.text)
        print (about_the_creator.text)
        home_button = self.browser.find_element(*Buttons.home_button)
        home_button.click()
        time.sleep(1)
        print("About page test is done")

if __name__ == '__main__':
    unittest.main(verbosity=1)