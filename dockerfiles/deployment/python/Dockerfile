FROM python:3-alpine
WORKDIR /service
COPY requirements.txt .
COPY app.py
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]
