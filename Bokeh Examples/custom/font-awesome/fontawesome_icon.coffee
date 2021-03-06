{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from bokeh.charts import output_notebook, show\n",
    "from bokeh.charts.glyphs import BarGlyph\n",
    "\n",
    "output_notebook()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Composite Glyph\n",
    "\n",
    "One or more actual glyphs that have been grouped together to represent some set of data, which respond to some standardized set of graphics operations.\n",
    "\n",
    "In a chart, a composite glyph is generated for each group of data. For example, a box glyph will produce one box for a box plot. This is composed of multiple glyphs, but represents a single group of data.\n",
    "\n",
    "This guide walks through the creation and use of composite glyphs."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## BarGlyph\n",
    "\n",
    "A simple bar has two components. It has some location along an axis, then it has some height from that axis. A bar can be created from a single value, or it can be created through aggregation. For example:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Bar from single value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "bar = BarGlyph(label='a', values=[1])\n",
    "bar.data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Bar from multiple values\n",
    "\n",
    "Notice the difference in height."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "bar = BarGlyph(label='a', values=[1, 2, 3, 4])\n",
    "bar.data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Simplified input using same order"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "bar = BarGlyph('a', 1)\n",
    "bar.data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Operations on Composite Glyphs\n",
    "\n",
    "Grammar of Graphics describes some common graphical operations that each glyph type would respond differently to. A common operation for bars would be stacking"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Un-Stacked"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "bar1 = BarGlyph('foo', 1)\n",
    "bar2 = BarGlyph('foo', 2)\n",
    "\n",
    "print('No stacking')\n",
    "print('bar1 y: %s, bar2 y: %s' % (bar1.data['y'], bar2.data['y']) )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Stacked"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from bokeh.charts.operations import stack\n",
    "\n",
    "bar1, bar2 = stack(bar1, bar2)\n",
    "\n",
    "print('With Stacking')\n",
    "print('bar1 y: %s, bar2 y: %s' % (bar1.data['y'], bar2.data['y']) )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Producing Combined Data Source"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from bokeh.charts.utils import comp_glyphs_to_df\n",
    "\n",
    "# utility that uses pandas.concat to concatenate each CompositeGlyph.df\n",
    "comp_glyphs_to_df(bar1, bar2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Standalone Use of Composite Glyphs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from bokeh.charts.chart import Chart\n",
    "from bokeh.models.ranges import DataRange1d, FactorRange\n",
    "from bokeh.io import curdoc, curstate\n",
    "\n",
    "def add_chart_to_doc(chart):\n",
    "    \"Handle adding chart to doc.\"\n",
    "    curdoc()._current_plot = chart\n",
    "    curdoc().add_root(chart)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Build Bars and Add Them Manually to Chart\n",
    "\n",
    "In the chart below, the bars corresponding to `foo` overlap."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "\n",
    "# two bars overlap on the same label/index\n",
    "bar1 = BarGlyph(label='foo', values=[1])\n",
    "bar2 = BarGlyph('foo', 2)\n",
    "\n",
    "# only the third bar doesn't overlap\n",
    "bar3 = BarGlyph('bar', 3)\n",
    "\n",
    "# composite glyphs can have multiple renderers, so we get them all\n",
    "renderers = []\n",
    "for bar in [bar1, bar2, bar3]:\n",
    "    renderers += bar.renderers\n",
    "\n",
    "# create a chart and directly add the renderers\n",
    "c = Chart(renderers=renderers)\n",
    "\n",
    "# add ranges/scales (typically handled by builder)\n",
    "c.add_ranges('x', FactorRange(factors=['foo', 'bar']))\n",
    "c.add_ranges('y', DataRange1d(start=0, end=4))\n",
    "\n",
    "c.add_scales('x', 'auto')\n",
    "c.add_scales('y', 'auto')\n",
    "\n",
    "# build the chart (typically called by create_and_build)\n",
    "c.start_plot()\n",
    "\n",
    "# add chart to doc (typically handled by create_and_build)\n",
    "add_chart_to_doc(c)\n",
    "\n",
    "show(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Stack the Bars, then Show Chart\n",
    "\n",
    "One potential way to handle overlapping bars is to stack them. See below that stacking the bars results in a stacked bar chart."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "stack(bar1, bar2, bar3)\n",
    "\n",
    "show(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
