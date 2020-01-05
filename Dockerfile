FROM python:3.4-alpine
RUN mkdir -p /opt/code
ADD . /opt/code
WORKDIR /opt/code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]