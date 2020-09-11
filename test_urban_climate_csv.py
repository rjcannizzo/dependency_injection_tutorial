import datetime
from pathlib import Path

from app import App
from urban_climate_csv import DataSource


BASE_DIR = Path(__file__).resolve(strict=True).parent


def test_read():
    app = App()
    for key, value in app.read(file_name=Path(BASE_DIR).joinpath('london.csv')).items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value