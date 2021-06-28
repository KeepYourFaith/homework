from app import db
import sqlalchemy


class Record(db.Model):
    __tablename__ = "record"
    id = db.Column(sqlalchemy.Integer, primary_key=True)
    ip_address = db.Column(sqlalchemy.String(64))
    time = db.Column(sqlalchemy.DateTime)
    operation = db.Column(sqlalchemy.Text())
    ret_code = db.Column(sqlalchemy.Integer)
    ret_content = db.Column(sqlalchemy.Text())

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item
