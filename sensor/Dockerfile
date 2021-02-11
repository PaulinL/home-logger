FROM python:3

# Create app directory
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./logger.py" ]
