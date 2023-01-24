FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --user -r requirements.txt


FROM python:3.11-slim-bullseye

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . /app

ENTRYPOINT ["python3"]
CMD ["main.py"]
