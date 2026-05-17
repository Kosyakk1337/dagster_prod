import pandas as pd
import numpy as np
from dagster import asset, get_dagster_logger

@asset
def generate_catering_dataframe() -> pd.DataFrame:
    np.random.seed(42)
    data = {
        "restaurant_id": range(1, 100),
        "daily_revenue_rub": np.random.uniform(10000, 250000, 99).round(2),
        "rating": np.random.uniform(2.0, 5.0, 99).round(1),
    }
    return pd.DataFrame(data)

@asset
def filter_dataframe(generate_catering_dataframe: pd.DataFrame) -> pd.DataFrame:
    return generate_catering_dataframe[generate_catering_dataframe["rating"] >= 4.5]