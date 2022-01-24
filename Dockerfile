from python:3.10.1

WORKDIR /usr/src/app

LABEL org.opencontainers.image.authors="ronald.buder@gmail.com"

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY config.py .
COPY main.py .

ENTRYPOINT ["python", "main.py"]