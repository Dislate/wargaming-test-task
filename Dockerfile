FROM python:3.8-alpine

WORKDIR /app

COPY reqirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

VOLUME [ "/app" ]

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]