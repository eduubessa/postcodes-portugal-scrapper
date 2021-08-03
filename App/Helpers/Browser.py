from random import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Browser:

    url = "https://www.codigo-postal.pt/"

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.driver.get(self.url)
            random.randint(3, 8)
        except Exception as ex:
            print("Chrome Driver is not working...")

    def all_districts_select(self):
        el_districts = self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[1]/ul/li')
        for el_district in el_districts:
            print(el_district.find_element_by_tag_name("a").text)


browser = Browser()
browser.all_districts_select()