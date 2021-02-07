From python:3.6-stretch

WORKDIR /backend

ADD . /backend

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uwsgi", "app.ini"]