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
    IbHeader = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(4) h3")
    IbInput = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(4) [type]")
    TbHeader = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(5) h3")
    TbInput = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(5) [type]")
    CHeader = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(6) h3")
    CInput = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(6) [type]")
    InHeader = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(7) h3")
    InInput = (By.CSS_SELECTOR, ".flexbox-container .box:nth-of-type(7) [type]")

class ShortReadsPage():
    article1 = (By.LINK_TEXT, "Calorie Control")
    article2 = (By.PARTIAL_LINK_TEXT, "Tool")
    article3 = (By.PARTIAL_LINK_TEXT, "Seasoning")
    header = (By.CSS_SELECTOR, "h3")

