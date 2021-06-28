from flasky import db
from app.models import Record
from datetime import datetime
import pytz


def insert_to_record(ip_addr, operation, code, msg):
    cn_tz = pytz.timezone('Asia/Shanghai')
    time = datetime.now().replace(tzinfo=cn_tz)
    record = Record(ip_address=ip_addr,
                    operation=operation,
                    time=time,
                    ret_code=code,
                    ret_content=msg)
    db.session.add(record)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return e
    return 0
