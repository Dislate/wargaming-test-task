FROM python:3.8-alpine

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache build-base

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

VOLUME [ "/app" ]

CMD [ ""]
CMD [ "flask", "run" ]