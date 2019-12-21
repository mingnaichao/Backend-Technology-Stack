FROM python:3.6

MAINTAINER mingnaichao<mingnaichao@qq.com>

ADD ./requirements.txt requirements.txt
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

ADD . /docker_test
WORKDIR /docker_test

CMD python app.py

EXPOSE 30534
