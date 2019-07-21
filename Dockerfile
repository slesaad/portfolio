FROM python:3.7

WORKDIR /code

RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs

RUN npm install -g sass

COPY requirements.txt /code

RUN pip install -r requirements.txt

COPY . /code
