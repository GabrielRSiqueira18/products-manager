from selenium.webdriver.remote.webelement import WebElement

from Selenium import Selenium
from utils.global_variables import global_web_commerces

if __name__ == '__main__':
    s = Selenium(global_web_commerces[0])

    elements: list[WebElement] = s.search_products()


