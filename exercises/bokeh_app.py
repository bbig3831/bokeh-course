from bokeh.models import Slider, ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.plotting import figure
from numpy.random import random

initial_points = 500
data_points = ColumnDataSource(
    data={'x': random(initial_points), 'y': random(initial_points)}
)

plot = figure(title='Random scatter plot generator')
plot.diamond(x='x', y='y', source=data_points, color='red')
slider_widget = Slider(start=0, end=10000, step=10, value=initial_points,
                       title='Slide right to increase number of points')

def callback(attr, old, new):
    points = slider_widget.value
    data_points.data = {'x': random(points), 'y': random(points)}

slider_widget.on_change('value', callback)

# Create layout
layout = row(slider_widget, plot)
curdoc().add_root(layout)