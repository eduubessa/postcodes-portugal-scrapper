import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from App.Models.County import County
from App.Models.District import District


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
            District.district = el_district.find_element_by_tag_name("a").text
            District.save()

    def all_counties_select(self):
        el_districts = self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[1]/ul/li')
        for el_district in el_districts:
            district_select = el_district.find_element_by_tag_name("a").text
            el_district.find_element_by_tag_name("a").click()
            time.sleep(random.randint(3, 8))
            el_counties = self.driver.find_elements_by_xpath("//*[@id=\"district\"]/div/div[1]/div/ul/li")
            district_data = District.where('district', district_select).first()
            for el_county in el_counties:
                print(el_county.find_element_by_tag_name("a").text)
                County.district = district_data["id"]
                County.county = el_county.find_element_by_tag_name("a").text
                County.save()
                self.driver.execute_script("window.history.go(-1)")




    def __del__(self):
        self.driver.close()