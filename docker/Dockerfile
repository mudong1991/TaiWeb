FROM daocloud.io/python:2.7
MAINTAINER mudong  <blog.scmud.com>
ENV PYPYTHONUNBUFFERED 1
ADD taileizi.tar /var/www/taileizi
WORKDIR /var/www/taileizi
RUN pip install  -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com