from .new_job import pandas_etl_job, pandas_etl_schedule
from .ops_and_jobs import random_array_job

# Собираем всё в списки, чтобы легко импортировать в definitions.py
all_jobs = [pandas_etl_job, random_array_job]

all_schedules = [pandas_etl_schedule]