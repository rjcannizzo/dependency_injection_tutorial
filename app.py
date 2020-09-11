"""
Dependency injection tutorial
https://testdriven.io/blog/python-dependency-injection/
9-11-2020
"""
import csv
from datetime import datetime
from pathlib import Path
import matplotlib.dates
import matplotlib.pyplot

BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    def read(self, filename):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(filename)) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                hour = datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour

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
    filename = sys.argv[1]
    app = App()
    d = app.read(filename)
    app.draw(d)
