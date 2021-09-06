FROM python:3.7

COPY ./requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
