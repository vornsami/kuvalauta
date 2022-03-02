FROM python:3.9.10-buster

WORKDIR /usr/src/app
COPY . ./

RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

RUN echo "\napp.run(host='0.0.0.0')"  >>  application/__init__.py
EXPOSE 5000

CMD python run.py