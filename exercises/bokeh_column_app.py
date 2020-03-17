import os
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.io import curdoc
from bokeh.layouts import row
# from config import base_dir


df = pd.read_csv(os.path.join('/home/ben/Documents/online_classes/oreilly/bokeh-viz','data','sandp500','all_stocks_5yr.csv'))
df_apple = df[df['Name'] == 'AAL']

# Create the ColumnDataSource object
data = ColumnDataSource(data={
    'x': df_apple['high'],
    'y': df_apple['low'],
    'x1': df_apple['volume']
})

plot = figure(title='Attribute selector application')
plot.diamond('x', 'y', source=data, color='red')
select_widget = Select(
    options=['low', 'volume'],
    value='low',
    title='Select a new y axis attribute'
)

def callback(attr, old, new):
    if new == 'low':
        data.data = {'x': df_apple['high'], 'y': df_apple['low']}
    else:
        data.data = {'x': df_apple['high'], 'y': df_apple['volume']}

select_widget.on_change('value', callback)

layout = row(select_widget, plot)
curdoc().add_root(layout)