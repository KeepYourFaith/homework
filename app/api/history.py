import math
from flask import session
from flasky import Record


def query_filter(page=1, per_page=10):
    ip_addr = session.get("ip_addr")
    begin_time = session.get("begin_time")
    end_time = session.get("end_time")
    ret_code = session.get("ret_code") if session.get("ret_code") else None
    if len(str(ip_addr)) > 1000 or len(str(begin_time)) > 1000 or len(str(end_time)) > 1000 or len(str(ret_code)) > 1000:
        return 300001, None, None
    attr = ""
    if ip_addr:
        attr += "Record.ip_address=='" + str(ip_addr) + "',"
    if begin_time:
        attr += "Record.time>='" + str(begin_time) + "',"
    if end_time:
        attr += "Record.time<='" + str(end_time) + "',"
    if ret_code is not None:
        attr += "Record.ret_code==" + str(ret_code) + ","
    sql = "Record.query.filter("+attr[0:-1]+")"
    if attr:
        records = eval(sql)
    else:
        records = Record.query
    pages = 0
    if not session.get("pages"):
        pages = math.ceil(records.count() / per_page)
    if page > pages:
        page = 1
    records = records.offset((page - 1) * per_page).limit(per_page).all()
    json_records = []
    for i in records:
        json_records.append(i.to_json())
    return 0, math.ceil(pages/per_page), json_records


