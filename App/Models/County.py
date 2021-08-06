from Database.DB import DB

class County:
    __table = "counties"

    district = None
    county = None
    scrapped = False

    __data = None
    __query = None

    @staticmethod
    def all():
        db = DB()
        return db.table(County.__table).select().all()

    @staticmethod
    def where(field, value, condition="LIKE"):
        db = DB()
        if County.__query is None:
            County.__query = db.table(County.__table).select().where(field, value, condition)
        else:
            County.__query = County.__query.where(field, value, condition)
        return County

    @staticmethod
    def get():
        result = County.__query.get()
        County.__query = None
        return result

    @staticmethod
    def first():
        db = DB()
        if County.__query is None:
            return db.table(County.__table).select().first()
        else:
            return County.__query.first()

    @staticmethod
    def last():
        db = DB()
        return db.table(County.__table).select().last()

    @staticmethod
    def save():
        data = [
            ['district_id', County.district],
            ['county', County.county],
            ['scrapped', County.scrapped]
        ]
        db = DB()
        return db.table(County.__table).insert(data)

    @staticmethod
    def update():
        data = [
            ['district_id', County.district],
            ['county', County.county],
            ['scrapped', County.scrapped]
        ]
        db = DB()
        return County.__query.update(data)

