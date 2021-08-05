import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from App.Models.County import County
from App.Models.District import District
from App.Models.Parish import Parish


class Browser:
    url = "https://www.codigo-postal.pt/"

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.driver.get(self.url)
            random.randint(3, 8)
        except Exception as ex:
            print("Chrome Driver is not working...")

    # fetch all district on website and save on database
    def all_districts(self):
        el_districts = self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[1]/ul/li')
        for el_district in el_districts:
            print(el_district.find_element_by_tag_name("a").text)
            District.district = el_district.find_element_by_tag_name("a").text
            District.save()

    # fetch all counties on website and save on database
    def fetch_all_counties(self, district):
        el_counties = self.driver.find_elements_by_xpath('//*[@id="district"]/div/div[1]/div/ul/li')
        for el_county in el_counties:
            County.district = district["id"]
            County.county = el_county.find_element_by_tag_name("a").text
            County.save()

    # fetch all parishes on website
    def fetch_all_parishes(self, district, county):
        el_parishes = self.driver.find_elements_by_xpath('//*[@id="county"]/div/div[1]/div[1]/ul/li')
        for el_parish in el_parishes:
            Parish.district = district["id"]
            Parish.county = county["id"]
            Parish.parish = el_parish.find_element_by_tag_name("a").text
            Parish.save()

    # Fetch all counties by district on website
    def fetch_all_counties_by_district(self, district):
        el_districts = self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[1]/ul/li')
        for el_district in el_districts:
            x = el_district.find_element_by_tag_name("a").text
            if x == district:
                return el_district.find_element_by_tag_name("a").get_attribute("href")

    # Fetch all parishes by county on website
    def fetch_all_parishes_by_county(self, county):
        el_counties = self.driver.find_elements_by_xpath('//*[@id="district"]/div/div[1]/div/ul/li')
        for el_county in el_counties:
            x = el_county.find_element_by_tag_name("a").text
            if x == county:
                return el_county.find_element_by_tag_name("a").get_attribute("href")

    def fetch_all_postcodes_by_parish(self, parish):
        el_postcodes = self.driver.find_elements_by_xpath('//*[@id="isolated"]/div/p[@class="odd"]')
        for el_postcode in el_postcodes:
            x = el_postcode.find_elements_by_xpath('span[3]/a').text
            print(x)


    def navigation_to(self, to):
        if to is not None:
            self.driver.get(str(to))
        else:
            return None

    def back_page(self):
        self.driver.execute_script("window.history.go(-1)")

    def __del__(self):
        self.driver.close()
