import pandas as pd
from dagster import asset, get_dagster_logger
from dagster_aws.s3 import S3Resource

@asset
def raw_data() -> pd.DataFrame:
    """Генерирует исходный DataFrame на 30 строк."""
    logger = get_dagster_logger()
    logger.info("Генерируем сырые данные...")
    data = {"id": range(1, 31), "value": [x * 10 for x in range(1, 31)]}
    return pd.DataFrame(data)

@asset
def filtered_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """Фильтрует DataFrame, оставляя только значения больше 150."""
    logger = get_dagster_logger()
    filtered_df = raw_data[raw_data["value"] > 150]
    logger.info(f"Осталось строк после фильтрации: {len(filtered_df)}")
    return filtered_df

@asset
def upload_to_s3(filtered_data: pd.DataFrame, s3: S3Resource) -> None:
    """Явно сохраняет отфильтрованный DataFrame в S3 (MinIO) в виде CSV-файла."""
    logger = get_dagster_logger()
    
    # Конвертируем DataFrame в строку формата CSV
    csv_data = filtered_data.to_csv(index=False)
    
    # Получаем boto3 клиент из ресурса и загружаем файл
    s3_client = s3.get_client()
    s3_client.put_object(
        Bucket="dagster-data",
        Key="manual_exports/filtered_data.csv",
        Body=csv_data
    )
    logger.info("Файл успешно загружен в MinIO по пути: dagster-data/manual_exports/filtered_data.csv")