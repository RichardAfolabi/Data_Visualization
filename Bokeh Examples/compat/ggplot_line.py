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
    "import pandas as pd\n",
    "import numpy as np\n",
    "from bokeh.charts import Dot, output_notebook, show"
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
    "# create some example data\n",
    "data = {\n",
    "    'sample': ['lists', 'loops', 'dicts', 'gen exp', 'exceptions']*3,\n",
    "    'interpreter': [item for name in ['python', 'pypy', 'jython'] for item in [name]*5],\n",
    "    'timing': [2, 3, 7, 5, 26, 12, 33, 47, 15, 126, 22, 43, 10, 25, 26],\n",
    "}"
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
    "dots = Dot(data, values='timing', label='interpreter',\n",
    "           group='sample', title=\"Dots Example, dict input\",\n",
    "           ylabel='Performance', legend='top_left')\n",
    "show(dots)"
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
    "df = pd.DataFrame(data)\n",
    "dots = Dot(df, values='timing', label='interpreter',\n",
    "           group='sample', title=\"Dots Example, pandas input\",\n",
    "           ylabel='Performance', legend='top_left')\n",
    "show(dots)"
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
