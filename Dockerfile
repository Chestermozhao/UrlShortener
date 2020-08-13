FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY . /url_shortener
COPY entrypoint.sh /entrypoint.sh
WORKDIR /url_shortener

RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "/entrypoint.sh"]

EXPOSE 8000
