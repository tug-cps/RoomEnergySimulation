FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# enable color support
ENV TERM xterm-256color
# disable buffered stdout
ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "model"]
