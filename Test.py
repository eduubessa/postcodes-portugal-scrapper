import random
import time
import pymysql
from App.Helpers.Config import Config
from App.Helpers.Browser import Browser

browser = Browser()
connection = None

try:
    connection = pymysql.connect(port=Config.get('database.port', 3306),
                                 host=Config.get('database.host', 'localhost'),
                                 user=Config.get('database.username', 'root'),
                                 password=Config.get('database.password', ''),
                                 database=Config.get('database.database'),
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        sql = "SELECT * FROM `districts` WHERE scrapped = FALSE;"
        cursor.execute(sql)
        districts = cursor.fetchall()

        for district in districts:
            to = browser.fetch_all_counties_by_district(district["district"])
            browser.navigation_to(to)
            with connection.cursor() as cursor:

                sql = "SELECT * FROM `counties` WHERE scrapped = FALSE AND `district_id` = %s;"
                cursor.execute(sql, (district["id"]))
                counties = cursor.fetchall()

                for county in counties:
                    to = browser.fetch_all_parishes_by_county(county["county"])
                    browser.navigation_to(to)

                    with connection.cursor() as cursor:
                        sql = "SELECT * FROM `parishes` WHERE scrapped = FALSE AND `district_id` = %s AND `county_id`= %s;"
                        cursor.execute(sql, (district["id"], county["id"]))
                        parishes = cursor.fetchall()

                        for parish in parishes:
                            to = browser.fetch_all_postcodes_by_parish(parish["parish"])
                            browser.navigation_to(to)
                            time.sleep(random.randint(1, 3))
                            browser.fetch_all_postcodes(district, county, parish)
                            sql = "UPDATE `parishes` SET `scrapped` = %s WHERE `id` = %s"
                            connection.commit()
                            cursor.execute(sql, (True, parish['id']))
                            browser.county_page()
                            time.sleep(random.randint(1, 2))

                        with connection.cursor() as cursor:
                            sql = "UPDATE `counties` SET `scrapped` = %s WHERE `id` = %s"
                            connection.commit()
                            cursor.execute(sql, (True, county['id']))

                        browser.district_page()

                    with connection.cursor() as cursor:
                        sql = "UPDATE `districts` SET `scrapped` = %s WHERE `id` = %s"
                        connection.commit()
                        cursor.execute(sql, (True, district['id']))

except Exception as ex:
    print("MySql Connection Error:")
    print(ex)

finally:
    connection.close()
