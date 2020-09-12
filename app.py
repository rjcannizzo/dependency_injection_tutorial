"""
Dependency injection tutorial
https://testdriven.io/blog/python-dependency-injection/
9-11-2020
"""
from datetime import datetime
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    def __init__(self, data_source, plot):
        self.data_source = data_source
        self.plot = plot

    def read(self, **kwargs):
        return self.data_source.read(**kwargs)

    def draw(self, temps_by_hour):
        dates = []
        temperatures = []
        for date, temperature in temps_by_hour.items():
            dates.append(datetime.fromisoformat(date))
            temperatures.append(temperature)

        self.plot.draw(dates, temperatures)

    @classmethod
    def configure(cls, filename):
        with open(filename) as file:
            config = json.load(file)

        data_source = __import__(config['data_source']['name']).DataSource()
        plot = __import__(config['plot']['name']).Plot()
        return cls(data_source, plot)


if __name__ == '__main__':
    import sys

    config_file = sys.argv[1]
    file_name = sys.argv[2]
    app = App.configure(config_file)
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)
