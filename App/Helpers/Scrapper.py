import random
import time

from App.Helpers.Browser import Browser
from App.Models.County import County
from App.Models.District import District
from App.Models.Parish import Parish


class Scrapper:

    @staticmethod
    def fetch_districts():
        if District.where('scrapped', False).get() is not None:
            browser = Browser()
            browser.all_districts()
        else:
            return False

    @staticmethod
    def fetch_counties():
        print("fetch counties")
        browser = Browser()
        # Fetch all districts
        districts = District.where('scrapped', False).get()
        for district in districts:
            to = browser.fetch_all_counties_by_district(district["district"])
            browser.navigation_to(to)
            browser.fetch_all_counties(district)
            print(district)
            browser.back_page()
            time.sleep(random.randint(3, 6))

    @staticmethod
    def fetch_parishes():
        browser = Browser()
        # Fetch all districts
        districts = District.where('scrapped', False).get()
        counties = County.where('scrapped', False).get()
        for district in districts:
            for county in counties:
                if district["id"] == county["district_id"]:
                    to = browser.fetch_all_counties_by_district(district["district"])
                    browser.navigation_to(to)
                    to = browser.fetch_all_parishes_by_county(county["county"])
                    browser.navigation_to(to)
                    browser.fetch_all_parishes(district, county)
                    time.sleep(random.randint(2, 3))
                    browser.back_page()
                    time.sleep(random.randint(3, 6))

    @staticmethod
    def fetch_postcodes():
        browser = Browser()
        # Fetch all districts
        districts = District.where('scrapped', False).get()
        for district in districts:
            to = browser.fetch_all_counties_by_district(district["district"])
            browser.navigation_to(to)
            # Fetch all counties by district
            counties = County.where('district_id', district["id"]).get()
            # Loop in counties
            for county in counties:
                to = browser.fetch_all_parishes_by_county(county["county"])
                browser.navigation_to(to)
                # Fetch all parishes by county
                time.sleep(3)
                parishes = Parish.where('county_id', county["id"]).get()
                # Loop on parishes fetch all postcodes
                for parish in parishes:
                    to = browser.fetch_all_postcodes_by_parish(parish["parish"])
                    browser.navigation_to(to)
                    browser.fetch_all_postcodes(district, county, parish)
                    browser.county_page()
                    time.sleep(2)
            browser.district_page()
            time.sleep(10)








