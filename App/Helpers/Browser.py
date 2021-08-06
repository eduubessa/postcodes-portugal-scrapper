import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from App.Models.County import County
from App.Models.District import District
from App.Models.Parish import Parish
from App.Models.Postcode import Postcode


class Browser:
    url = 'https://www.codigo-postal.pt/'

    def __init__(self):
        try:
            options = Options()
            self.driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager().install())
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
        el_parishes = self.driver.find_elements_by_xpath('//*[@id="county"]/div/div[1]/div/ul/li')
        for el_parish in el_parishes:
            Parish.district = district["id"]
            Parish.county = county["id"]
            Parish.parish = el_parish.find_element_by_tag_name("a").text
            Parish.save()

    # fetch all Postcodes on website and save on database
    def fetch_all_postcodes(self, district, county, parish):
        while True:
            el_postcodes = self.driver.find_elements_by_xpath('//*[@id="isolated"]/div/p')
            for el_postcode in el_postcodes:
                if el_postcode.text is not None and el_postcode.text != "":
                    x = str(el_postcode.text)
                    x = x.splitlines()
                    Postcode.district = district["id"]
                    Postcode.county = county["id"]
                    Postcode.parish = parish["id"]
                    Postcode.postcode = x[2].split(" ")[0]
                    Postcode.address = x[1]
                    Postcode.location = x[3]
                    Postcode.coords = x[0].replace("GPS: ", "")
                    Postcode.save()
            time.sleep(random.randint(2, 4))
            try:
                self.driver.find_element_by_css_selector('.pagination li.next a').click()
            except:
                time.sleep(2)
                break

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
        el_parishes = self.driver.find_elements_by_xpath('//*[@id="county"]/div/div[1]/div/ul/li')
        for el_parish in el_parishes:
            x = el_parish.find_element_by_tag_name("a").text
            if x == parish:
                return el_parish.find_element_by_tag_name("a").get_attribute("href")

    def next_page(self):
        self.driver.find_element_by_css_selector('.pagination > li.next > a').click()

    def county_page(self):
        self.driver.find_element_by_css_selector('.breadcrumbs a:nth-child(2)').click()

    def district_page(self):
        self.driver.find_element_by_css_selector('.breadcrumbs a:first-child').click()

    def initial_page(self):
        self.navigation_to(self.url)

    def navigation_to(self, to):
        if to is not None:
            self.driver.get(str(to))
        else:
            return None

    def back_page(self):
        self.driver.execute_script("window.history.go(-1)")

    def __del__(self):
        self.driver.close()
