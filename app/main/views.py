from flask import session, request, jsonify
from . import main
from app.api.download import download_file_by_url, delet_file
from app.api.runCmd import cmd_run
from app.api.history import query_filter
from app.api.db_op import insert_to_record
from config import PER_PAGE


@main.route('/download/<int:cover>', methods=['GET', 'POST'])
def download(cover=None):
    url_addr = request.form.get("address") if request.form.get("address") else ""
    code, msg = download_file_by_url(url_addr, cover)
    # 将用户操作结果插入数据库
    ret = insert_to_record(request.remote_addr, "download:" + url_addr, str(code), msg)
    if ret == 0:
        return jsonify(code=code, message=msg)
    else:
        if code == 0:
            # 删除下载的文件
            delet_file(url_addr)
    return jsonify(code=2, message=str(ret))


@main.route('/cmd', methods=["GET", "POST"])
def run_cmd():
    cmd = request.form.get("cmd") if request.form.get("cmd") else ""
    code, msg = cmd_run(cmd)
    ret = insert_to_record(request.remote_addr, "run cmd:" + cmd, str(code), msg)
    if ret == 0:
        return jsonify(code=code, message=msg)
    else:
        return jsonify(code=2, message=str(ret))


@main.route("/history/<int:page>", methods=["GET", "POST"])
def search_history(page=None):
    if request.method == "POST":
        page = 1
        session["pages"] = None
        session["ip_addr"] = request.form.get("ip_addr")
        session["begin_time"] = request.form.get("begin_time")
        session["end_time"] = request.form.get("end_time")
        session["ret_code"] = request.form.get("ret_code") if request.form.get("ret_code") else None
    if page is None or page <= 0:
        page = 1
    code, pages, page_data = query_filter(page=page, per_page=PER_PAGE)
    ret = insert_to_record(request.remote_addr, "history: " +
                           " method=" + request.method +
                           " page=" + str(page) +
                           " ip="+ str(session.get("ip_addr")) +
                           " begin_time=" + str(session.get("begin_time")) +
                           " end_time=" + str(session.get("end_time")) +
                           " ret_code=" + str(session.get("ret_code")),
                           0, "查询成功")

    if ret == 0:
        if code == 0:
            return jsonify(code=code, message={"pages": pages, "result": page_data})
        else:
            return jsonify(code=code, message=None)
    else:
        return jsonify(code=2, message=str(ret))



