<h1 align="center">Url shorten service</h1>

<p align="center">
<a href="https://travis-ci.com/caiyunapp/caiyun-weather-dashboard">
<img alt="Build Status"
src="https://travis-ci.com/caiyunapp/caiyun-weather-dashboard.svg?token=W2LJe9sYpF9SfStseQx6&branch=master"></a>
<a href="https://github.com/psf/black">
<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# Build and Run server with Docker
- `docker build -t url_shortener:latest .`
- `docker run -e HOST_HOSTNAME=localhost -p 8000:8000 url_shortener`
- swagger doc: open `http://localhost:8000` on your chrome browser

# Start service with Python
- `python3 -m venv venv`
- `source venv/bin/activate`
- Install dependencies
  - `pip install -r requirements.txt`
  - `pip install poetry;poetry install`
  - `pre-commit install`

- Run server with uvicorn
  - `uvicorn url_shortener.main:app --port 8000 --host 0.0.0.0`

# How to use
- You can create a short URL by POST [/shortener/](http://localhost:8000/shortener/).
- After getting the short URL, you can request it and get the website.
![./images/demo.gif](./images/demo.gif)

# Test
- Run test cases
  - `pytest tests/test_doc.py`
  - `pytest tests/test_shorten_url.py`
- CI: travis
