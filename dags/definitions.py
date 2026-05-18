import os
from dagster import Definitions, load_assets_from_package_module
from dagster_aws.s3 import s3_pickle_io_manager, S3Resource

# Импортируем наши папки (пакеты)
from . import assets

# Импортируем готовые списки из нашей папки с джобами
from .ops_and_jobs import all_jobs, all_schedules

# 1. Автоматически загружаем все ассеты
all_assets = load_assets_from_package_module(assets)

# 2. Регистрируем всё вместе
defs = Definitions(
    assets=all_assets,
    jobs=all_jobs,
    schedules=all_schedules,
    resources={
        "io_manager": s3_pickle_io_manager.configured({
            "s3_bucket": "dagster-data",
            "s3_prefix": "assets",
        }),
        "s3": S3Resource(
            endpoint_url=os.environ.get("AWS_ENDPOINT_URL", "http://minio:9000"),
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        )
    }
)