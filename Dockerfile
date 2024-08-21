FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /briefing_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "/briefing_api/script.sh"]