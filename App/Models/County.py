from Database.DB import DB


class County:
    __table = "counties"

    district = 0
    county = None
    scrapped = False

    @staticmethod
    def all():
        print("Fectch all rows")

    @staticmethod
    def get():
        print("Get rows")

    @staticmethod
    def save():
        data = [
            ['district_id', County.district],
            ['county', County.county],
            ['scrapped', County.scrapped]
        ]
        db = DB()
        db.table(County.__table).insert(data)
