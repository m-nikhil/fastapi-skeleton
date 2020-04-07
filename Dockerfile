FROM python:3.7

COPY . /

EXPOSE 8000

RUN pip3 install pipenv

# Docker don't need a virtual environment within it.
RUN pipenv lock -r > deploy-requirements.txt
RUN pip3 install -r deploy-requirements.txt

CMD gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0