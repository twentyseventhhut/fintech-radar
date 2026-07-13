# Tiny always-on Telegram webhook receiver (stdlib only — no pip deps).
FROM python:3.12-slim
WORKDIR /app
COPY webhook.py /app/webhook.py
ENV PORT=8080
CMD ["python3", "webhook.py"]
