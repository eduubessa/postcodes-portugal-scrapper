from Database.DB import DB

class Postcode:
    __table = "postcodes"

    district = None
    county = None
    parish = None
    postcode = None
    address = None
    location = None
    coords = None
    scrapped = False

    __data = None
    __query = None

    @staticmethod
    def all():
        db = DB()
        return db.table(Postcode.__table).select().all()

    @staticmethod
    def where(field, value, condition="LIKE"):
        db = DB()
        if Postcode.__query is None:
            Postcode.__query = db.table(Postcode.__table).select().where(field, value, condition)
        else:
            Postcode.__query = Postcode.__query.where(field, value, condition)
        return Postcode

    @staticmethod
    def get():
        return Postcode.__query.get()

    @staticmethod
    def first():
        db = DB()
        if Postcode.__query is None:
            return db.table(Postcode.__table).select().first()
        else:
            return Postcode.__query.first()

    @staticmethod
    def last():
        db = DB()
        return db.table(Postcode.__table).select().last()

    @staticmethod
    def save():
        data = [
            ['district_id', Postcode.district],
            ['county_id', Postcode.county],
            ['parish_id', Postcode.parish],
            ['postcode', Postcode.postcode],
            ['address', Postcode.address],
            ['location', Postcode.location],
            ['coords', Postcode.coords],
        ]
        db = DB()
        return db.table(Postcode.__table).insert(data)

    @staticmethod
    def update():
        data = [
            ['district_id', Postcode.district],
            ['county_id', Postcode.county],
            ['parish_id', Postcode.parish],
            ['postcode', Postcode.postcode],
            ['address', Postcode.address],
            ['location', Postcode.location],
            ['coords', Postcode.coords],
        ]
        db = DB()
        return Postcode.__query.update(data)

