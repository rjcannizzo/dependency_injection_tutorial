"""
Dependency injection tutorial
https://testdriven.io/blog/python-dependency-injection/
9-11-2020
"""
from datetime import datetime
from pathlib import Path
import matplotlib.dates
import matplotlib.pyplot

BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    def __init__(self, data_source):
        self.data_source = data_source

    def read(self, **kwargs):
        return self.data_source.read(**kwargs)

    def draw(self, temperatures_by_hour):
        dates = []
        temperatures = []
        for date, temperature in temperatures_by_hour.items():
            dates.append(datetime.fromisoformat(date))
            temperatures.append(temperature)

        dates = matplotlib.dates.date2num(dates)
        matplotlib.pyplot.plot_date(dates, temperatures, linestyle='-')
        matplotlib.pyplot.show()


if __name__ == '__main__':
    import sys
    from open_weather_json import DataSource

    file_name = sys.argv[1]
    app = App(DataSource())
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)
