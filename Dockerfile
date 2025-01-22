FROM python:3.7

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN rm -rf /tmp

CMD ["python", "/home/app/shopping_list/bootstrapping.py"]
