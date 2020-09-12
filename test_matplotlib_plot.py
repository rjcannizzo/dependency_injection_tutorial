import datetime
from unittest.mock import MagicMock

import matplotlib.pyplot

from matplotlib_plot import Plot


def test_draw(monkeypatch):
    plot_date_mock = MagicMock()
    show_mock = MagicMock()
    monkeypatch.setattr(matplotlib.pyplot, 'plot_date', plot_date_mock)
    monkeypatch.setattr(matplotlib.pyplot, 'show', show_mock)

    plot = Plot()
    hours = [datetime.datetime.now()]
    temperatures = [14.52]
    plot.draw(hours,  temperatures)

    _, called_temperatures = plot_date_mock.call_args[0]
    assert called_temperatures == temperatures  # check that plot_date was called with temperatures as second arg
    show_mock.assert_called()  # check that show is called