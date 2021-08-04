import random
import time

from App.Helpers.Browser import Browser
from App.Models.County import County
from App.Models.District import District


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
        for district in districts:
            counties = County.where('district_id', 1).get()
            for county in counties:
                browser.fetch_all_parishes_by_county(county["county"])