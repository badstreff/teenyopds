FROM python:3.8-alpine
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main
CMD ["flask", "run", "--host=0.0.0.0"]