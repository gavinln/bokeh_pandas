from __future__ import print_function

from collections import OrderedDict

from bokeh.plotting import figure, output_server, show, push
from bokeh.sampledata import us_counties
from bokeh.models import HoverTool

from bokeh.plotting import cursession
import bokeh
import time

county_xs = [
    us_counties.data[code]['lons'] for code in us_counties.data
    if us_counties.data[code]['state'] in ['tx']
]

county_ys = [
    us_counties.data[code]['lats'] for code in us_counties.data
    if us_counties.data[code]['state'] in ['tx']
]

import us_regions_state_boundaries

xs, ys, names = us_regions_state_boundaries.main()

output_server("us_state")

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"


def createFigure():
    fig = figure(title="US Map", tools=TOOLS)

    excludeList = ['Alaska']

    for idx in range(len(xs)):
        region, state = names[idx]

        if len(region) > 0 and state not in excludeList:
            fig.patches(xs[idx], ys[idx], fill_alpha=0.7,
                        line_color="white", line_width=0.5,
                        fill_color="green", name=state)
    return fig


def set_color(fig, name, newColor):
    rendererList = fig.select(dict(name=name))
    oldColor = None
    for renderer in rendererList:
        oldColor = renderer.glyph.fill_color
        renderer.glyph.fill_color = newColor

    for renderer in rendererList:
        renderer._dirty = True
        cursession().store_objects(renderer)
        renderer.data_source._dirty = True
        cursession().store_objects(renderer.data_source)

    return oldColor


fig = createFigure()
#show(fig)
push()


def update():
    time.sleep(1)
    newColor = bokeh.enums.NamedColor._values[43]
    print('About to set color')
    oldColor = set_color(fig, 'Colorado', newColor)
    time.sleep(1)
    set_color(fig, 'California', oldColor)
    time.sleep(1)


# bokeh.enums.NamedColor._values[43]

def get_renderer():
    renderer = fig.select(dict(name='Colorado'))
    return renderer[0]


def get_session():
    return cursession()

#hover = p.select(dict(type=HoverTool))
#hover.snap_to_data = False
#hover.tooltips = OrderedDict([
#    ("index", "$index"),
#])
#
