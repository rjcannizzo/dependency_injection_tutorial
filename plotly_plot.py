import plotly.graph_objects


class Plot:

    def draw(self, hours, temperatures):
        fig = plotly.graph_objects.Figure(
            data=[plotly.graph_objects.Scatter(x=hours, y=temperatures)]
        )
        fig.show()
