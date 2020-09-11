import datetime
from pathlib import Path
from unittest.mock import MagicMock
import matplotlib.pyplot
from app import App

BASE_DIR = Path(__file__).resolve(strict=True).parent


def test_read():
    hour = datetime.datetime.now().isoformat()
    temperature = 14.52
    temperature_by_hour = {hour: temperature}

    data_source = MagicMock()
    data_source.read.return_value = temperature_by_hour
    app = App(
        data_source=data_source
    )
    assert app.read(file_name='something.csv') == temperature_by_hour


def test_draw(monkeypatch):
    plot_date_mock = MagicMock()
    show_mock = MagicMock()
    monkeypatch.setattr(matplotlib.pyplot, 'plot_date', plot_date_mock)
    monkeypatch.setattr(matplotlib.pyplot, 'show', show_mock)

    app = App(MagicMock())
    hour = datetime.datetime.now().isoformat()
    temperature = 14.52
    app.draw({hour: temperature})

    _, called_temperatures = plot_date_mock.call_args[0]
    assert called_temperatures == [temperature]  # check that plot_date was called with temperatures as second arg
    show_mock.assert_called()  # check that show is called