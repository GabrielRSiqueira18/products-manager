import time

from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from utils import GlobalWebCommerces, QUANTITY_ELEMENTS_PER_SEARCH
from selenium.webdriver.support import expected_conditions as EC

class Selenium(webdriver.Chrome):
    def __init__(self, e_commerce: GlobalWebCommerces):
        self.__data = e_commerce
        self.__timeout = 6

        service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        super().__init__(service=service, options=chrome_options)
        self.get(e_commerce.url)

    def search_products(self, query_search: str) -> list[WebElement] or None:
        data = self.__data.scrapping_details

        input_element = WebDriverWait(self, self.__timeout).until(
            EC.presence_of_element_located((data.input_tag_type, data.input_tag))
        )
        input_element.send_keys(query_search)
        submit_button = self.find_element(
            data.submit_button_tag_type,
            data.submit_button_tag
        )
        submit_button.click()

        result = []
        try:
            elements = WebDriverWait(self, self.__timeout).until(
                EC.presence_of_all_elements_located((data.result_tag_type, data.result_tag))
            )

            for element in elements[:QUANTITY_ELEMENTS_PER_SEARCH]:
                try:
                    product_name = element.find_element(data.product_name_tag_type, data.product_name_tag).text
                    price = element.find_element(data.price_tag_type, data.price_tag).text
                    symbol = element.find_element(data.symbol_tag_type, data.symbol_tag).text
                    image = element.find_element(data.image_tag_type, data.image_tag).get_attribute("src")
                    link = element.find_element(data.link_tag_type, data.link_tag).get_attribute("href")

                    print(f"{product_name} - {symbol}{price} - {image} - {link}\n")
                    result.append({
                        'product_name': product_name,
                        'symbol': symbol,
                        'price': price,
                        'image': image,
                        'link': link,
                    })
                except:
                    continue
                finally:
                    return result

        except TimeoutException:
            return None