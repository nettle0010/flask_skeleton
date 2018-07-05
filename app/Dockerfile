FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /usr/src/app/src
CMD ["uwsgi","--ini","/usr/src/app/uwsgi.ini"]
