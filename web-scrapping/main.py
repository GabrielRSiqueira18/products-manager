from queue import Queue

from Selenium import Selenium
from utils.global_variables import global_web_commerces, TIME_TO_SEARCH_IN_SECONDS
import time
from ScrappingThread import ScrappingThread

if __name__ == '__main__':
    queue_products = Queue()


    for web_commerce in global_web_commerces:
        s = Selenium(web_commerce)
        scrapping_thread = ScrappingThread(web_commerce, s, queue_products)
        scrapping_thread.start()

    while(True):
        if queue_products.empty() is not True:
             product = queue_products.get()
             print(product)


