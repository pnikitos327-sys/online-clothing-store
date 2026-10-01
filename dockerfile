FROM python:3.11-slim

WORKDIR /app

COPY /app requirements.txt

RUN pip install requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]

