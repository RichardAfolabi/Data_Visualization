{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from bokeh.charts import Horizon, output_notebook, show"
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
    "# Here is some code to read in some stock data from the Yahoo Finance API\n",
    "AAPL = pd.read_csv(\n",
    "    \"http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010\",\n",
    "    parse_dates=['Date'])\n",
    "MSFT = pd.read_csv(\n",
    "    \"http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2010\",\n",
    "    parse_dates=['Date'])\n",
    "IBM = pd.read_csv(\n",
    "    \"http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2010\",\n",
    "    parse_dates=['Date'])\n",
    "\n",
    "data = dict(\n",
    "    AAPL=AAPL['Adj Close'],\n",
    "    Date=AAPL['Date'],\n",
    "    MSFT=MSFT['Adj Close'],\n",
    "    IBM=IBM['Adj Close'],\n",
    ")"
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
    "h = Horizon(data, x='Date', title=\"horizon plot using stock inputs\",\n",
    "            width=800, height=300)\n",
    "show(h)"
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
    "# example with random data\n",
    "import numpy as np\n",
    "\n",
    "x = np.linspace(0, np.pi*4, 137)\n",
    "y = (2*np.random.normal(size=137) + x**2)\n",
    "xx = np.hstack([-1*x[::-1], x])\n",
    "yy = np.hstack([-1*y[::-1], y])\n",
    "data = dict(x=xx, y=yy, y2=yy, y3=yy, y4=yy, y5=yy)\n",
    "h = Horizon(data, x='x', title=\"test horizon\", ylabel='Random')\n",
    "show(h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
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
