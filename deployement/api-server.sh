#!bin/bash

echo "starting the service"

HOST="0.0.0.0"
PORT=8000
WORKERS=4
LOG_LEVEL="info"
APP_MODULE="main:app"

uvicorn $APP_MODULE --host $HOST --port $PORT --loop "uvloop" --http "httptools" --log-level $LOG_LEVEL --access-log --proxy-headers --forwarded-allow-ips="*"
