import datetime
from pathlib import Path
from unittest.mock import MagicMock
import matplotlib.pyplot
from app import App

BASE_DIR = Path(__file__).resolve(strict=True).parent


def test_read():
    app = App()
    data_file = Path(BASE_DIR).joinpath('london.csv')
    for key, value in app.read(filename=data_file).items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value


def test_draw(monkeypatch):
    plot_date_mock = MagicMock()
    show_mock = MagicMock()
    monkeypatch.setattr(matplotlib.pyplot, 'plot_date', plot_date_mock)
    monkeypatch.setattr(matplotlib.pyplot, 'show', show_mock)

    app = App()
    hour = datetime.datetime.now().isoformat()
    temperature = 14.52
    app.draw({hour: temperature})
    _, called_temperatures = plot_date_mock.call_args[0]
    assert called_temperatures == [temperature]
    show_mock.assert_called()
