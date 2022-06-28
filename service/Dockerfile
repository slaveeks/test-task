FROM python:3.8.10-slim-buster

WORKDIR /home/app

RUN pip install --upgrade pip
COPY ./service/ .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
