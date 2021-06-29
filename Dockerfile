FROM python:3.6

ENV FLASK_APP flasky.py

WORKDIR /home/baidi

COPY requirements.txt ./
# 安装python虚拟环境
RUN pip install -r requirements.txt

COPY app app
COPY download_files download_files
COPY migrations migrations
COPY flasky.py config.py ./

EXPOSE 12345
CMD flask run --host 0.0.0.0 --port 12345