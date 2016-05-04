# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:43:23 2016

@author: rpjai
"""

from bokeh.io import curdoc
from bokeh.plotting import Figure, output_file, show, ColumnDataSource
# from bokeh.models import HBox
from bokeh.models.widgets import Slider, Select
from bokeh.sampledata.autompg import autompg as am

auto_src = ColumnDataSource(data=dict(xs=am.mpg, ys=am.hp))

p1 = Figure(plot_width=400, plot_height=400)
p1.scatter('xs', 'ys', source=auto_src)

x_select = Select(title="", options=['mpg', 'weight', 'accel'], value="accel")
y_select = Select(title="", options=['mpg', 'weight', 'accel'], value="mpg")

def update_plot(attrname, old, new):
    new_x, new_y = x_select.value, y_select.value
    pass

# 1. ColumnDataSource(x, y)
# 2. Create scatter ()
# 3. x, y Select widgets.
# 4. Update function.

#
# my_slider = Slider(start=0, end=100, step=1, value=50, title="Circle Radius")
#
# def update_size(attrname, old, new):
#     new_sz = [my_slider.value]
#     cir_source.data = dict(x1=cir_x, y1=cir_y, sz=new_sz)
#
# for w in [my_slider]:
#     w.on_change('value', update_size)
#
# hlayout = HBox(my_slider, p1)

output_file('auto_scatter.html')
# curdoc().add_root(hlayout)
show(p1)