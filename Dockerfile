FROM python:slim

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["python3", "detournement.py"]
