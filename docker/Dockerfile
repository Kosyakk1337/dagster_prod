FROM python:3.10-slim

ENV DAGSTER_HOME=/opt/dagster/dagster_home
ENV PYTHONPATH=/opt/dagster/app

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

WORKDIR /opt/dagster/app

# Устанавливаем системные зависимости, если нужно (например, для компиляции драйверов БД)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY dags/requirements.txt ./dags/
RUN pip install --no-cache-dir -r ./dags/requirements.txt

# Копируем системные конфиги
COPY docker/workspace.yaml /opt/dagster/dagster_home/
COPY docker/dagster.yaml /opt/dagster/dagster_home/

# Копируем код (для продакшен сборок, локально будет перекрыто volume)
COPY dags/ ./dags/