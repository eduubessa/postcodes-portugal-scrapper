from Database.DB import DB

class District:
    __table = "districts"

    district = None
    scrapped = False

    __selected = False
    __query = None
    __last_method = None

    @staticmethod
    def all():
        db = DB()
        return db.table(District.__table).select().all()

    @staticmethod
    def where(field, value, condition="LIKE"):
        db = DB()
        if District.__selected is False:
            District.__query = db.table(District.__table).select().where(field, value, condition)
        else:
            District.__query = District.__query.where(field, value, condition)
        return District

    @staticmethod
    def get():
        db = DB()
        return db.table(District.__table).select().get()

    @staticmethod
    def first():
        db = DB()
        if District.__query is None:
            return db.table(District.__table).select().first()
        else:
            return District.__query.first()

    def last():
        db = DB()
        return db.table(District.__table).select().last()

    @staticmethod
    def save():
        data = [
            ['district', District.district],
            ['scrapped', District.scrapped]
        ]
        db = DB()
        db.table(District.__table).insert(data)

    @staticmethod
    def update(data):
        return District.__query.update(data)

