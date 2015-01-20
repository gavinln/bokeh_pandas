from __future__ import print_function

import time

from numpy import pi, sin, linspace

from bokeh.document import Document
from bokeh.models.glyphs import Line
from bokeh.models import Plot, DataRange1d, ColumnDataSource
from bokeh.session import Session
from bokeh.models import GlyphRenderer


def get_source(x):
    x_static = linspace(-2*pi, 2*pi, 1000)
    y = sin(x)

    source = ColumnDataSource(data=dict(x=x, y=y, x_static=x_static))
    return source


def plot_line(session, document, source, color):
    session.load_document(document)
    xdr_static = DataRange1d(sources=[source.columns("x_static")])
    ydr = DataRange1d(sources=[source.columns("y")])

    plot = Plot(x_range=xdr_static, y_range=ydr, min_border=50)
    line_glyph = Line(x="x", y="y", line_color=color)
    plot.add_glyph(source, line_glyph)
    document.add(plot)
    session.store_document(document)
    return plot


def animate(session, plot):
    'updates data '
    renderer = plot.select(dict(type=GlyphRenderer))
    ds = renderer[0].data_source

    for i in linspace(-pi/2.0, 0, 10):
        ds.data['x'] = x + i
        session.store_objects(ds)
        time.sleep(0.5)


def update(session, plot):
    ' updates line color only after a browser refresh '
    renderer = plot.select(dict(type=GlyphRenderer))
    glyph = renderer[0].glyph
    glyph.line_color = 'red'
    session.store_objects(glyph)


session = Session()
session.use_doc('animated_line2')

x = linspace(-2*pi, 2*pi, 1000)
source = get_source(x)
document = Document()
plot = plot_line(session, document, source, 'blue')
animate(session, plot)
update(session, plot)
