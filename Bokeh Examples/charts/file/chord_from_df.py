{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Plotting contents of an Excel File\n",
    "\n",
    "This notebook simply demonstrates how to plot the contents of an excel file using pandas an the bokeh `bokeh.charts` high level interface"
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
    "import pandas as pd\n",
    "\n",
    "filepath = \"http://databank.worldbank.org/data/download/catalog/climate_change_download_0.xls\""
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
    "df = pd.ExcelFile(filepath).parse('Data')"
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
    "emissions = df[df['Series name'] == \"CO2 emissions, total (KtCO2)\"].copy()\n",
    "for k in [2007, 2006, 2005]:\n",
    "    emissions[k] = pd.to_numeric(emissions[k], errors='coerce')\n",
    "\n",
    "emissions = emissions.sort_values(2007, ascending=False)\n",
    "_remissions = emissions.iloc[:10, :]"
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
    "columns = ['Country code', 'Country name', 2007, 2006, 2005]\n",
    "remissions = _remissions[columns]\n",
    "remissions.columns = [str(x) for x in remissions.columns]"
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
    "from bokeh.plotting import figure, show, output_notebook, output_server, curdoc\n",
    "from bokeh.sampledata.autompg import autompg as df\n",
    "from bokeh.charts import Bar\n",
    "from bokeh.charts.operations import blend\n",
    "\n",
    "output_notebook()"
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
    "palette = ['#f7fcf5', '#e5f5e0','#c7e9c0', '#a1d99b','#74c476','#41ab5d','#238b45','#005a32', '#5A6351', '#000000']\n",
    "\n",
    "p = Bar(remissions, label='years', group='Country name', palette=palette,\n",
    "        values= blend('2007', '2006', '2005', name='values', labels_name='years'),\n",
    "        title='Emissions', color='Country name', legend=True, responsive=True)\n",
    "show(p)"
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
    "greys = ['#ffffff', '#f0f0f0', '#d9d9d9', '#bdbdbd', '#969696', '#737373', '#525252', '#252525', '#000000']\n",
    "blues = [\"#f7fbff\" ,\"#deebf7\" ,\"#c6dbef\" ,\"#9ecae1\" ,\"#6baed6\" ,\"#4292c6\" ,\"#2171b5\" ,\"#084594\"]\n",
    "p = Bar(remissions, label='Country name', group='year', palette = blues[1::3],\n",
    "        values= blend('2007', '2006', '2005', name='values', labels_name='year'),\n",
    "        title='Emissions', color='year', legend=True, responsive=True)\n",
    "show(p)"
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
