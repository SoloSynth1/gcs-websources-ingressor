FROM python:3.7-alpine

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

ENV APP_HOME /app
ENV PORT 8080

WORKDIR $APP_HOME
COPY . .

CMD python3 app.py