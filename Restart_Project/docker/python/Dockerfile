FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /Restart
WORKDIR /Restart
ADD requirements.txt /Restart/
RUN pip install -r requirements.txt
ADD . /Restart/