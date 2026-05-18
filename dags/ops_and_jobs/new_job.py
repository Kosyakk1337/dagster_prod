from dagster import define_asset_job, AssetSelection, ScheduleDefinition

# Dagster сам найдет переменную pandas_etl_job благодаря нашему скрипту
pandas_etl_job = define_asset_job(
    name="pandas_s3_etl_job",
    selection=AssetSelection.keys("raw_data", "filtered_data", "upload_to_s3")
)

# Dagster автоматически найдет и расписание!
pandas_etl_schedule = ScheduleDefinition(
    job=pandas_etl_job,
    cron_schedule="0 * * * *", # Запуск каждый час
)