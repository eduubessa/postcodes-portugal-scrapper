from Database.DB import DB

class Parish:
    __table = "parishes"

    district = None
    county = None
    parish = None
    scrapped = False

    __data = None
    __query = None

    @staticmethod
    def all():
        db = DB()
        return db.table(Parish.__table).select().all()

    @staticmethod
    def where(field, value, condition="LIKE"):
        db = DB()
        if Parish.__query is None:
            Parish.__query = db.table(Parish.__table).select().where(field, value, condition)
        else:
            Parish.__query = Parish.__query.where(field, value, condition)
        return Parish

    @staticmethod
    def get():
        return Parish.__query.get()

    @staticmethod
    def first():
        db = DB()
        if Parish.__query is None:
            return db.table(Parish.__table).select().first()
        else:
            return Parish.__query.first()

    @staticmethod
    def last():
        db = DB()
        return db.table(Parish.__table).select().last()

    @staticmethod
    def save():
        data = [
            ['district_id', Parish.district],
            ['county_id', Parish.county],
            ['Parish', Parish.parish],
            ['scrapped', Parish.scrapped]
        ]
        db = DB()
        return db.table(Parish.__table).insert(data)

    @staticmethod
    def update():
        data = [
            ['district_id', Parish.district],
            ['county_id', Parish.county],
            ['parish', Parish.parish],
            ['scrapped', Parish.scrapped]
        ]
        db = DB()
        return Parish.__query.update(data)

