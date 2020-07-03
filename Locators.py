from selenium.webdriver.common.by import By

class HomePage():
    about_link = (By.LINK_TEXT, "About")
    calc_link = (By.LINK_TEXT, "Calculator")
    logo = (By.XPATH, "/html//div[@id='root']//h1[.='Kitchen Calculator']")

class CalculatorPage():
    ozHeader = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(3) h3")
    ozInput = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(3) [type]")
