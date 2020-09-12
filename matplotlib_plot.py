import matplotlib.dates
import matplotlib.pyplot


class Plot:
    def draw(self, hours, temperatures):
        hours = matplotlib.dates.date2num(hours)
        matplotlib.pyplot.plot_date(hours, temperatures, linestyle='-')
        matplotlib.pyplot.show(block=True)
