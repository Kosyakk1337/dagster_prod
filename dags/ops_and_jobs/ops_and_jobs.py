import random
from dagster import op, job, get_dagster_logger

@op
def generate_random_array() -> list[int]:
    """Генерирует случайный массив из 10 чисел."""
    logger = get_dagster_logger()
    arr = [random.randint(1, 100) for _ in range(10)]
    logger.info(f"Сгенерирован массив: {arr}")
    return arr

@op
def print_array(arr: list[int]) -> None:
    """Выводит (принтует) полученный массив в логи."""
    logger = get_dagster_logger()
    logger.info(f"Получен массив из предыдущего шага: {arr}")

@job
def random_array_job():
    """Джоб, который связывает генерацию массива и его логирование."""
    print_array(generate_random_array())