FROM python:3

WORKDIR /usr/src/app


COPY db.py .
RUN pip3 install psycopg2

CMD ["python","db.py"]

