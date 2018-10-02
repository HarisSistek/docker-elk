FROM python:3.4-alpine

RUN mkdir code

COPY requirements.txt /code
COPY app.py /code

WORKDIR /code

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
