FROM python:3.12-slim-bullseye AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim-bullseye AS runtime

RUN apt-get update && apt-get install -y \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

WORKDIR /app

# Copy Python dependencies from builder stage
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY app/ ./app/
COPY run.py ./
COPY requirements.txt ./
COPY app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY app/gunicorn.conf.py ./gunicorn.conf.py

RUN chown -R appuser:appuser /app

RUN mkdir -p /var/log/supervisor && \
    chown -R appuser:appuser /var/log/supervisor

USER appuser

ENV PATH="/home/appuser/.local/bin:$PATH"

EXPOSE 8000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]