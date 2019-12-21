FROM python:3.6

MAINTAINER mingnc<mingnaichao@qq.com>

ADD ./requirements.txt requirements.txt
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

ADD . /chat_robot
WORKDIR /chat_robot


RUN apt-get update -y  && apt-get install -y tesseract-ocr libtesseract-dev libx11-xcb1 libaio1 libsasl2-dev python-dev libldap2-dev libssl-dev libevent-dev libblas-dev libatlas-base-dev libgtk-3-dev libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3  libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4  libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1  libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 libnss3



CMD python application.py

EXPOSE 8866
