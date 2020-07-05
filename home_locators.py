from selenium.webdriver.common.by import By

class HomePage():
    about_link = (By.LINK_TEXT, "About")
    calc_link = (By.LINK_TEXT, "Calculator")
    watch_link = (By.LINK_TEXT, "Watch")
    short_reads_link = (By.LINK_TEXT, "Short Reads")
    logo = (By.XPATH, "/html//div[@id='root']//h1[.='Kitchen Calculator']")

class Buttons():
    home_button = (By.LINK_TEXT, "Home")
    reads_button = (By.LINK_TEXT, "Reads")

class CalculatorPage():
    ozHeader = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(3) h3")
    ozInput = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(3) [type]")

