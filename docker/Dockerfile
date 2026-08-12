FROM python:3.12-slim

LABEL org.opencontainers.image.title="AI Cloud Labs CI/CD Application"
LABEL org.opencontainers.image.description="Containerized application for the Cloud DevOps CI/CD Platform"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd \
    --create-home \
    --uid 10001 \
    appuser

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .

RUN chown -R appuser:appuser /app

USER 10001

EXPOSE 8080

HEALTHCHECK \
    --interval=30s \
    --timeout=5s \
    --start-period=10s \
    --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')"

CMD ["python", "app.py"]
