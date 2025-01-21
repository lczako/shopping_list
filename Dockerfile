FROM python:3.7

ADD requirements.txt /tmp/requirements.txt
COPY shopping_list /home/app/src
COPY test /home/app/test

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN rm -rf /tmp
