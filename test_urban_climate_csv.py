import datetime
from pathlib import Path

from app import App
from urban_climate_csv import DataSource


BASE_DIR = Path(__file__).resolve(strict=True).parent


def test_read():
    reader = DataSource()
    for key, value in reader.read(file_name='london.csv').items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value