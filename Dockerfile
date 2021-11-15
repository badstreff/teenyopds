FROM python:3.8
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main
CMD ["python", "main.py"]