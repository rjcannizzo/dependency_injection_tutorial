import datetime
from unittest.mock import MagicMock

import plotly.graph_objects

from plotly_plot import Plot


def test_draw(monkeypatch):
    figure_mock = MagicMock()
    monkeypatch.setattr(plotly.graph_objects, 'Figure', figure_mock)
    scatter_mock = MagicMock()
    monkeypatch.setattr(plotly.graph_objects, 'Scatter', scatter_mock)

    plot = Plot()
    hours = [datetime.datetime.now()]
    temperatures = [14.52]
    plot.draw(hours, temperatures)

    call_kwargs = scatter_mock.call_args[1]
    assert call_kwargs['y'] == temperatures  # check that plot_date was called with temperatures as second arg
    figure_mock().show.assert_called()  # check that show is called
