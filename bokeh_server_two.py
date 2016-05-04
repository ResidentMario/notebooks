# -*- coding: utf-8 -*-

from bokeh.io import curdoc
from bokeh.plotting import Figure, output_file, show, ColumnDataSource
from bokeh.models import HBox
from bokeh.models.widgets import Slider, Select
# from bokeh.sampledata.autompg import autompg as am

cir_x=[10]
cir_y=[10]
cir_size=[10]

cir_source = ColumnDataSource(data=dict(
                                        x1=cir_x,
                                        y1=cir_y,
                                        sz=cir_size))

p1 = Figure(plot_width=300, plot_height=300)
p1.circle('x1', 'y1', size='sz', color='red', source=cir_source)

my_slider = Slider(start=0, end=100, step=1, value=50, title="Circle Radius")

def update_size(attrname, old, new):
    new_sz = [my_slider.value]
    cir_source.data = dict(x1=cir_x, y1=cir_y, sz=new_sz)

for w in [my_slider]:
    w.on_change('value', update_size)

hlayout = HBox(my_slider, p1)

output_file('circle1.html')
curdoc().add_root(hlayout)
#show(hlayout)