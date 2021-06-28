import os
import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects
from config import FILE_DOWNLOAD_PATH, TIME_OUT


def download_file_by_url(url, cover=None):
    # print(url)
    if not url:
        return 100006, "url不能为空"
    if len(url) > 10000:
        return 100007, "url过长"
    try:
        r = requests.get(url, timeout=TIME_OUT)
    except ConnectionError:
        return 100000, "连接错误"
    except HTTPError:
        return 100001, "http错误"
    except Timeout:
        return 100002, "连接超时"
    except TooManyRedirects:
        return 100003, "重定向错误"
    except Exception:
        return 100008, "下载失败"
    if r.status_code != 200:
        return 100004, "http请求错误"
    file_name = url.split('/')[-1]
    existing_file_names = os.listdir(FILE_DOWNLOAD_PATH)
    if file_name in existing_file_names and cover != 1:
        return 100005, "文件已存在"
    try:
        open(FILE_DOWNLOAD_PATH + file_name, 'wb').write(r.content)
    except IOError:
        return 1, "io错误"
    return 0, "文件下载完成"


# def message_askyesno(file_name):
#     top = tkinter.Tk()
#     top.withdraw()
#     top.update()
#     txt=messagebox.askquestion("提示", file_name+"已存在，是否覆盖原来的文件")
#     top.destroy()
#     print(txt)
#     return txt


def get_file_name(file_name):
    existing_file_names = os.listdir(FILE_DOWNLOAD_PATH)
    index = 0
    suffix = file_name.split('.')[-1]
    name = file_name.split('.')[0]
    while file_name in existing_file_names:
        index += 1
        file_name = str(name) + '(' + str(index) + ').' + suffix
    return file_name


def delet_file(url):
    file_name = url.split('/')[-1]
    os.remove(FILE_DOWNLOAD_PATH + file_name)


if __name__ == "__main__":
    pass
