import threading
import time
from utils.GlobalWebCommerces import GlobalWebCommerces
from Selenium import Selenium

class ScrappingThread(threading.Thread):
    def __init__(self, data: GlobalWebCommerces, selenium: Selenium, queue):
        super(ScrappingThread, self).__init__()
        self.__name = data.name
        self.__id = data.url
        self.__queue = queue
        self.__selenium = selenium

    def run(self):
        print("Starting scrapping thread: " + self.__name)

        while (True):
            result = self.__selenium.search_products("computador")
            if result:
                self.__queue.put(result)
            time.sleep(10)