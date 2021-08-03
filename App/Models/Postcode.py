from Database.DB import DB

class Postcode:

    __table = "postcodes"

    postcode = None
    district = None
    county = None
    parish = None
    longitude = None
    latitude = None


    @staticmethod
    def all():
        print("Fectch all rows")

    def get(self):
        print("Get rows")

    @staticmethod
    def save():
        data = [
                ['postcode', Postcode.postcode],
                ['district', Postcode.district],
                ['county', Postcode.county],
                ['parish', Postcode.parish],
                ['longitude', Postcode.longitude],
                ['latitude', Postcode.latitude]
            ]
        db = DB()
        db.table(Postcode.__table).insert(data)