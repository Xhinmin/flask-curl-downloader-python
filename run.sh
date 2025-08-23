#!/bin/bash
# 每分鐘清理 /tmp
while true; do
  find /tmp -mindepth 1 -delete
  sleep 86400
done &
# 啟動 Flask
exec python app.py