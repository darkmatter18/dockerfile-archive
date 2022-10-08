FROM python:3.9-slim as bigimage
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && pip wheel --wheel-dir=/root/wheels -r /app/requirements.txt


FROM python:3.9-slim as smallimage
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY --from=bigimage /root/wheels /root/wheels
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && pip install \
      --no-index \
      --find-links=/root/wheels --no-cache-dir -r /app/requirements.txt
COPY . /app
EXPOSE 8000
ENTRYPOINT gunicorn -b 0.0.0.0:8000 app.wsgi:application