{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from bokeh.plotting import figure, output_notebook, show\n",
    "from bokeh.models import ColumnDataSource, HoverTool, CustomJS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "    <div class=\"bk-root\">\n",
       "        <a href=\"http://bokeh.pydata.org\" target=\"_blank\" class=\"bk-logo bk-logo-small bk-logo-notebook\"></a>\n",
       "        <span id=\"56277a02-eb16-48c5-8ae8-96aa76cd05b8\">Loading BokehJS ...</span>\n",
       "    </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "(function(global) {\n",
       "  function now() {\n",
       "    return new Date();\n",
       "  }\n",
       "\n",
       "  var force = true;\n",
       "\n",
       "  if (typeof (window._bokeh_onload_callbacks) === \"undefined\" || force === true) {\n",
       "    window._bokeh_onload_callbacks = [];\n",
       "    window._bokeh_is_loading = undefined;\n",
       "  }\n",
       "\n",
       "\n",
       "  \n",
       "  if (typeof (window._bokeh_timeout) === \"undefined\" || force === true) {\n",
       "    window._bokeh_timeout = Date.now() + 5000;\n",
       "    window._bokeh_failed_load = false;\n",
       "  }\n",
       "\n",
       "  var NB_LOAD_WARNING = {'data': {'text/html':\n",
       "     \"<div style='background-color: #fdd'>\\n\"+\n",
       "     \"<p>\\n\"+\n",
       "     \"BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \\n\"+\n",
       "     \"may be due to a slow or bad network connection. Possible fixes:\\n\"+\n",
       "     \"</p>\\n\"+\n",
       "     \"<ul>\\n\"+\n",
       "     \"<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\\n\"+\n",
       "     \"<li>use INLINE resources instead, as so:</li>\\n\"+\n",
       "     \"</ul>\\n\"+\n",
       "     \"<code>\\n\"+\n",
       "     \"from bokeh.resources import INLINE\\n\"+\n",
       "     \"output_notebook(resources=INLINE)\\n\"+\n",
       "     \"</code>\\n\"+\n",
       "     \"</div>\"}};\n",
       "\n",
       "  function display_loaded() {\n",
       "    if (window.Bokeh !== undefined) {\n",
       "      document.getElementById(\"56277a02-eb16-48c5-8ae8-96aa76cd05b8\").textContent = \"BokehJS successfully loaded.\";\n",
       "    } else if (Date.now() < window._bokeh_timeout) {\n",
       "      setTimeout(display_loaded, 100)\n",
       "    }\n",
       "  }\n",
       "\n",
       "  function run_callbacks() {\n",
       "    window._bokeh_onload_callbacks.forEach(function(callback) { callback() });\n",
       "    delete window._bokeh_onload_callbacks\n",
       "    console.info(\"Bokeh: all callbacks have finished\");\n",
       "  }\n",
       "\n",
       "  function load_libs(js_urls, callback) {\n",
       "    window._bokeh_onload_callbacks.push(callback);\n",
       "    if (window._bokeh_is_loading > 0) {\n",
       "      console.log(\"Bokeh: BokehJS is being loaded, scheduling callback at\", now());\n",
       "      return null;\n",
       "    }\n",
       "    if (js_urls == null || js_urls.length === 0) {\n",
       "      run_callbacks();\n",
       "      return null;\n",
       "    }\n",
       "    console.log(\"Bokeh: BokehJS not loaded, scheduling load and callback at\", now());\n",
       "    window._bokeh_is_loading = js_urls.length;\n",
       "    for (var i = 0; i < js_urls.length; i++) {\n",
       "      var url = js_urls[i];\n",
       "      var s = document.createElement('script');\n",
       "      s.src = url;\n",
       "      s.async = false;\n",
       "      s.onreadystatechange = s.onload = function() {\n",
       "        window._bokeh_is_loading--;\n",
       "        if (window._bokeh_is_loading === 0) {\n",
       "          console.log(\"Bokeh: all BokehJS libraries loaded\");\n",
       "          run_callbacks()\n",
       "        }\n",
       "      };\n",
       "      s.onerror = function() {\n",
       "        console.warn(\"failed to load library \" + url);\n",
       "      };\n",
       "      console.log(\"Bokeh: injecting script tag for BokehJS library: \", url);\n",
       "      document.getElementsByTagName(\"head\")[0].appendChild(s);\n",
       "    }\n",
       "  };var element = document.getElementById(\"56277a02-eb16-48c5-8ae8-96aa76cd05b8\");\n",
       "  if (element == null) {\n",
       "    console.log(\"Bokeh: ERROR: autoload.js configured with elementid '56277a02-eb16-48c5-8ae8-96aa76cd05b8' but no matching script tag was found. \")\n",
       "    return false;\n",
       "  }\n",
       "\n",
       "  var js_urls = [\"https://cdn.pydata.org/bokeh/release/bokeh-0.12.4.min.js\", \"https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.4.min.js\"];\n",
       "\n",
       "  var inline_js = [\n",
       "    function(Bokeh) {\n",
       "      Bokeh.set_log_level(\"info\");\n",
       "    },\n",
       "    \n",
       "    function(Bokeh) {\n",
       "      \n",
       "      document.getElementById(\"56277a02-eb16-48c5-8ae8-96aa76cd05b8\").textContent = \"BokehJS is loading...\";\n",
       "    },\n",
       "    function(Bokeh) {\n",
       "      console.log(\"Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-0.12.4.min.css\");\n",
       "      Bokeh.embed.inject_css(\"https://cdn.pydata.org/bokeh/release/bokeh-0.12.4.min.css\");\n",
       "      console.log(\"Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.4.min.css\");\n",
       "      Bokeh.embed.inject_css(\"https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.4.min.css\");\n",
       "    }\n",
       "  ];\n",
       "\n",
       "  function run_inline_js() {\n",
       "    \n",
       "    if ((window.Bokeh !== undefined) || (force === true)) {\n",
       "      for (var i = 0; i < inline_js.length; i++) {\n",
       "        inline_js[i](window.Bokeh);\n",
       "      }if (force === true) {\n",
       "        display_loaded();\n",
       "      }} else if (Date.now() < window._bokeh_timeout) {\n",
       "      setTimeout(run_inline_js, 100);\n",
       "    } else if (!window._bokeh_failed_load) {\n",
       "      console.log(\"Bokeh: BokehJS failed to load within specified timeout.\");\n",
       "      window._bokeh_failed_load = true;\n",
       "    } else if (force !== true) {\n",
       "      var cell = $(document.getElementById(\"56277a02-eb16-48c5-8ae8-96aa76cd05b8\")).parents('.cell').data().cell;\n",
       "      cell.output_area.append_execute_result(NB_LOAD_WARNING)\n",
       "    }\n",
       "\n",
       "  }\n",
       "\n",
       "  if (window._bokeh_is_loading === 0) {\n",
       "    console.log(\"Bokeh: BokehJS loaded, going straight to plotting\");\n",
       "    run_inline_js();\n",
       "  } else {\n",
       "    load_libs(js_urls, function() {\n",
       "      console.log(\"Bokeh: BokehJS plotting callback run at\", now());\n",
       "      run_inline_js();\n",
       "    });\n",
       "  }\n",
       "}(this));"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "output_notebook()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# define some points and a little graph between them\n",
    "x = [2, 3, 5, 6, 8, 7]\n",
    "y = [6, 4, 3, 8, 7, 5]\n",
    "links = {\n",
    "    0: [1, 2],\n",
    "    1: [0, 3, 4],\n",
    "    2: [0, 5],\n",
    "    3: [1, 4],\n",
    "    4: [1, 3],\n",
    "    5: [2, 3, 4]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p = figure(width=400, height=400, tools=\"\", toolbar_location=None, title='Hover over points')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "source = ColumnDataSource({'x0': [], 'y0': [], 'x1': [], 'y1': []})\n",
    "sr = p.segment(x0='x0', y0='y0', x1='x1', y1='y1', color='olive', alpha=0.6, line_width=3, source=source, )\n",
    "cr = p.circle(x, y, color='olive', size=30, alpha=0.4, hover_color='olive', hover_alpha=1.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Add a hover tool, that sets the link data for a hovered circle\n",
    "code = \"\"\"\n",
    "var links = %s;\n",
    "var data = {'x0': [], 'y0': [], 'x1': [], 'y1': []};\n",
    "var cdata = circle.data;\n",
    "var indices = cb_data.index['1d'].indices;\n",
    "for (i=0; i < indices.length; i++) {\n",
    "    ind0 = indices[i]\n",
    "    for (j=0; j < links[ind0].length; j++) {\n",
    "        ind1 = links[ind0][j];\n",
    "        data['x0'].push(cdata.x[ind0]);\n",
    "        data['y0'].push(cdata.y[ind0]);\n",
    "        data['x1'].push(cdata.x[ind1]);\n",
    "        data['y1'].push(cdata.y[ind1]);\n",
    "    }\n",
    "}\n",
    "segment.data = data;\n",
    "\"\"\" % links\n",
    "\n",
    "callback = CustomJS(args={'circle': cr.data_source, 'segment': sr.data_source}, code=code)\n",
    "p.add_tools(HoverTool(tooltips=None, callback=callback, renderers=[cr]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "\n",
       "    <div class=\"bk-root\">\n",
       "        <div class=\"bk-plotdiv\" id=\"99ab87aa-696e-4cb6-ab89-f6bba1220db3\"></div>\n",
       "    </div>\n",
       "<script type=\"text/javascript\">\n",
       "  \n",
       "  (function(global) {\n",
       "    function now() {\n",
       "      return new Date();\n",
       "    }\n",
       "  \n",
       "    var force = false;\n",
       "  \n",
       "    if (typeof (window._bokeh_onload_callbacks) === \"undefined\" || force === true) {\n",
       "      window._bokeh_onload_callbacks = [];\n",
       "      window._bokeh_is_loading = undefined;\n",
       "    }\n",
       "  \n",
       "  \n",
       "    \n",
       "    if (typeof (window._bokeh_timeout) === \"undefined\" || force === true) {\n",
       "      window._bokeh_timeout = Date.now() + 0;\n",
       "      window._bokeh_failed_load = false;\n",
       "    }\n",
       "  \n",
       "    var NB_LOAD_WARNING = {'data': {'text/html':\n",
       "       \"<div style='background-color: #fdd'>\\n\"+\n",
       "       \"<p>\\n\"+\n",
       "       \"BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \\n\"+\n",
       "       \"may be due to a slow or bad network connection. Possible fixes:\\n\"+\n",
       "       \"</p>\\n\"+\n",
       "       \"<ul>\\n\"+\n",
       "       \"<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\\n\"+\n",
       "       \"<li>use INLINE resources instead, as so:</li>\\n\"+\n",
       "       \"</ul>\\n\"+\n",
       "       \"<code>\\n\"+\n",
       "       \"from bokeh.resources import INLINE\\n\"+\n",
       "       \"output_notebook(resources=INLINE)\\n\"+\n",
       "       \"</code>\\n\"+\n",
       "       \"</div>\"}};\n",
       "  \n",
       "    function display_loaded() {\n",
       "      if (window.Bokeh !== undefined) {\n",
       "        document.getElementById(\"99ab87aa-696e-4cb6-ab89-f6bba1220db3\").textContent = \"BokehJS successfully loaded.\";\n",
       "      } else if (Date.now() < window._bokeh_timeout) {\n",
       "        setTimeout(display_loaded, 100)\n",
       "      }\n",
       "    }\n",
       "  \n",
       "    function run_callbacks() {\n",
       "      window._bokeh_onload_callbacks.forEach(function(callback) { callback() });\n",
       "      delete window._bokeh_onload_callbacks\n",
       "      console.info(\"Bokeh: all callbacks have finished\");\n",
       "    }\n",
       "  \n",
       "    function load_libs(js_urls, callback) {\n",
       "      window._bokeh_onload_callbacks.push(callback);\n",
       "      if (window._bokeh_is_loading > 0) {\n",
       "        console.log(\"Bokeh: BokehJS is being loaded, scheduling callback at\", now());\n",
       "        return null;\n",
       "      }\n",
       "      if (js_urls == null || js_urls.length === 0) {\n",
       "        run_callbacks();\n",
       "        return null;\n",
       "      }\n",
       "      console.log(\"Bokeh: BokehJS not loaded, scheduling load and callback at\", now());\n",
       "      window._bokeh_is_loading = js_urls.length;\n",
       "      for (var i = 0; i < js_urls.length; i++) {\n",
       "        var url = js_urls[i];\n",
       "        var s = document.createElement('script');\n",
       "        s.src = url;\n",
       "        s.async = false;\n",
       "        s.onreadystatechange = s.onload = function() {\n",
       "          window._bokeh_is_loading--;\n",
       "          if (window._bokeh_is_loading === 0) {\n",
       "            console.log(\"Bokeh: all BokehJS libraries loaded\");\n",
       "            run_callbacks()\n",
       "          }\n",
       "        };\n",
       "        s.onerror = function() {\n",
       "          console.warn(\"failed to load library \" + url);\n",
       "        };\n",
       "        console.log(\"Bokeh: injecting script tag for BokehJS library: \", url);\n",
       "        document.getElementsByTagName(\"head\")[0].appendChild(s);\n",
       "      }\n",
       "    };var element = document.getElementById(\"99ab87aa-696e-4cb6-ab89-f6bba1220db3\");\n",
       "    if (element == null) {\n",
       "      console.log(\"Bokeh: ERROR: autoload.js configured with elementid '99ab87aa-696e-4cb6-ab89-f6bba1220db3' but no matching script tag was found. \")\n",
       "      return false;\n",
       "    }\n",
       "  \n",
       "    var js_urls = [];\n",
       "  \n",
       "    var inline_js = [\n",
       "      function(Bokeh) {\n",
       "        (function() {\n",
       "          var fn = function() {\n",
       "            var docs_json = {\"c2fc1c92-22fb-4307-b8ff-1027d3ad8841\":{\"roots\":{\"references\":[{\"attributes\":{},\"id\":\"eb94c1c4-78d3-4aaf-905f-a5e530aec80d\",\"type\":\"ToolEvents\"},{\"attributes\":{\"args\":{\"circle\":{\"id\":\"7668a888-2aa7-49e6-871a-f21ac52474e3\",\"type\":\"ColumnDataSource\"},\"segment\":{\"id\":\"73ea9b70-7dd5-4314-9746-55a145044f34\",\"type\":\"ColumnDataSource\"}},\"code\":\"\\nvar links = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1, 4], 4: [1, 3], 5: [2, 3, 4]};\\nvar data = {'x0': [], 'y0': [], 'x1': [], 'y1': []};\\nvar cdata = circle.data;\\nvar indices = cb_data.index['1d'].indices;\\nfor (i=0; i < indices.length; i++) {\\n    ind0 = indices[i]\\n    for (j=0; j < links[ind0].length; j++) {\\n        ind1 = links[ind0][j];\\n        data['x0'].push(cdata.x[ind0]);\\n        data['y0'].push(cdata.y[ind0]);\\n        data['x1'].push(cdata.x[ind1]);\\n        data['y1'].push(cdata.y[ind1]);\\n    }\\n}\\nsegment.data = data;\\n\"},\"id\":\"b634c281-c3f5-4111-9307-8931c2d74790\",\"type\":\"CustomJS\"},{\"attributes\":{\"line_alpha\":{\"value\":0.1},\"line_color\":{\"value\":\"#1f77b4\"},\"line_width\":{\"value\":3},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"0b2b59c4-f08e-415e-8cbe-6998748e7483\",\"type\":\"Segment\"},{\"attributes\":{\"callback\":null,\"column_names\":[\"y1\",\"y0\",\"x0\",\"x1\"],\"data\":{\"x0\":[],\"x1\":[],\"y0\":[],\"y1\":[]}},\"id\":\"73ea9b70-7dd5-4314-9746-55a145044f34\",\"type\":\"ColumnDataSource\"},{\"attributes\":{},\"id\":\"71be53e4-2b3a-4a45-b9fe-dd8e791cf80f\",\"type\":\"BasicTickFormatter\"},{\"attributes\":{\"plot\":null,\"text\":\"Hover over points\"},\"id\":\"4ac3bfee-9a0c-4c64-b4b4-9ed59a0a9123\",\"type\":\"Title\"},{\"attributes\":{\"fill_color\":{\"value\":\"olive\"},\"line_color\":{\"value\":\"olive\"},\"size\":{\"units\":\"screen\",\"value\":30},\"x\":{\"field\":\"x\"},\"y\":{\"field\":\"y\"}},\"id\":\"921b88f8-afdb-47cc-8e9f-e2839008c22b\",\"type\":\"Circle\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.1},\"fill_color\":{\"value\":\"#1f77b4\"},\"line_alpha\":{\"value\":0.1},\"line_color\":{\"value\":\"#1f77b4\"},\"size\":{\"units\":\"screen\",\"value\":30},\"x\":{\"field\":\"x\"},\"y\":{\"field\":\"y\"}},\"id\":\"33b59bae-0f2c-4d63-a886-28cf0a5f25db\",\"type\":\"Circle\"},{\"attributes\":{\"active_drag\":\"auto\",\"active_scroll\":\"auto\",\"active_tap\":\"auto\",\"tools\":[{\"id\":\"eadb0aa5-1428-47e3-90c6-d27ff59a95b1\",\"type\":\"HoverTool\"}]},\"id\":\"1421bda4-d552-49fd-b9bd-edac47a7faf9\",\"type\":\"Toolbar\"},{\"attributes\":{},\"id\":\"0b392046-29a9-4cbf-81d4-7a5566b3fc1d\",\"type\":\"BasicTicker\"},{\"attributes\":{},\"id\":\"4f4a0ca8-ea20-4bf4-8e49-570cae2c7c61\",\"type\":\"BasicTickFormatter\"},{\"attributes\":{\"plot\":{\"id\":\"6530201a-1af7-47fa-ba27-fad3748f71ac\",\"subtype\":\"Figure\",\"type\":\"Plot\"},\"ticker\":{\"id\":\"0b392046-29a9-4cbf-81d4-7a5566b3fc1d\",\"type\":\"BasicTicker\"}},\"id\":\"1b95d2ae-bc7b-4b5b-8c72-9fe2f87b4dae\",\"type\":\"Grid\"},{\"attributes\":{\"formatter\":{\"id\":\"71be53e4-2b3a-4a45-b9fe-dd8e791cf80f\",\"type\":\"BasicTickFormatter\"},\"plot\":{\"id\":\"6530201a-1af7-47fa-ba27-fad3748f71ac\",\"subtype\":\"Figure\",\"type\":\"Plot\"},\"ticker\":{\"id\":\"0e1e291d-7bd4-490a-861b-3f587466a4d3\",\"type\":\"BasicTicker\"}},\"id\":\"739794c1-1e59-4832-a0f4-676a0f8972cc\",\"type\":\"LinearAxis\"},{\"attributes\":{\"data_source\":{\"id\":\"73ea9b70-7dd5-4314-9746-55a145044f34\",\"type\":\"ColumnDataSource\"},\"glyph\":{\"id\":\"c87c4965-9ad7-4469-a9fb-d97f92ababc0\",\"type\":\"Segment\"},\"hover_glyph\":null,\"nonselection_glyph\":{\"id\":\"0b2b59c4-f08e-415e-8cbe-6998748e7483\",\"type\":\"Segment\"},\"selection_glyph\":null},\"id\":\"a1fde621-0908-4303-a223-64b77fe67515\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"callback\":null,\"column_names\":[\"x\",\"y\"],\"data\":{\"x\":[2,3,5,6,8,7],\"y\":[6,4,3,8,7,5]}},\"id\":\"7668a888-2aa7-49e6-871a-f21ac52474e3\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"callback\":null},\"id\":\"bb0e7510-e60e-40d2-bbcb-b466027f8a04\",\"type\":\"DataRange1d\"},{\"attributes\":{\"dimension\":1,\"plot\":{\"id\":\"6530201a-1af7-47fa-ba27-fad3748f71ac\",\"subtype\":\"Figure\",\"type\":\"Plot\"},\"ticker\":{\"id\":\"0e1e291d-7bd4-490a-861b-3f587466a4d3\",\"type\":\"BasicTicker\"}},\"id\":\"5b6725f2-bffb-45ad-88b8-4e65b5e7eea0\",\"type\":\"Grid\"},{\"attributes\":{\"callback\":{\"id\":\"b634c281-c3f5-4111-9307-8931c2d74790\",\"type\":\"CustomJS\"},\"plot\":{\"id\":\"6530201a-1af7-47fa-ba27-fad3748f71ac\",\"subtype\":\"Figure\",\"type\":\"Plot\"},\"renderers\":[{\"id\":\"79235b29-bb62-420c-b41f-5e3d9fff1dc8\",\"type\":\"GlyphRenderer\"}],\"tooltips\":null},\"id\":\"eadb0aa5-1428-47e3-90c6-d27ff59a95b1\",\"type\":\"HoverTool\"},{\"attributes\":{\"data_source\":{\"id\":\"7668a888-2aa7-49e6-871a-f21ac52474e3\",\"type\":\"ColumnDataSource\"},\"glyph\":{\"id\":\"477785c0-b9aa-4cde-883e-7ae231733df8\",\"type\":\"Circle\"},\"hover_glyph\":{\"id\":\"921b88f8-afdb-47cc-8e9f-e2839008c22b\",\"type\":\"Circle\"},\"nonselection_glyph\":{\"id\":\"33b59bae-0f2c-4d63-a886-28cf0a5f25db\",\"type\":\"Circle\"},\"selection_glyph\":null},\"id\":\"79235b29-bb62-420c-b41f-5e3d9fff1dc8\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.4},\"fill_color\":{\"value\":\"olive\"},\"line_alpha\":{\"value\":0.4},\"line_color\":{\"value\":\"olive\"},\"size\":{\"units\":\"screen\",\"value\":30},\"x\":{\"field\":\"x\"},\"y\":{\"field\":\"y\"}},\"id\":\"477785c0-b9aa-4cde-883e-7ae231733df8\",\"type\":\"Circle\"},{\"attributes\":{},\"id\":\"0e1e291d-7bd4-490a-861b-3f587466a4d3\",\"type\":\"BasicTicker\"},{\"attributes\":{\"below\":[{\"id\":\"b454a249-75b8-4669-be8e-9e45bb8defe0\",\"type\":\"LinearAxis\"}],\"left\":[{\"id\":\"739794c1-1e59-4832-a0f4-676a0f8972cc\",\"type\":\"LinearAxis\"}],\"plot_height\":400,\"plot_width\":400,\"renderers\":[{\"id\":\"b454a249-75b8-4669-be8e-9e45bb8defe0\",\"type\":\"LinearAxis\"},{\"id\":\"1b95d2ae-bc7b-4b5b-8c72-9fe2f87b4dae\",\"type\":\"Grid\"},{\"id\":\"739794c1-1e59-4832-a0f4-676a0f8972cc\",\"type\":\"LinearAxis\"},{\"id\":\"5b6725f2-bffb-45ad-88b8-4e65b5e7eea0\",\"type\":\"Grid\"},{\"id\":\"a1fde621-0908-4303-a223-64b77fe67515\",\"type\":\"GlyphRenderer\"},{\"id\":\"79235b29-bb62-420c-b41f-5e3d9fff1dc8\",\"type\":\"GlyphRenderer\"}],\"title\":{\"id\":\"4ac3bfee-9a0c-4c64-b4b4-9ed59a0a9123\",\"type\":\"Title\"},\"tool_events\":{\"id\":\"eb94c1c4-78d3-4aaf-905f-a5e530aec80d\",\"type\":\"ToolEvents\"},\"toolbar\":{\"id\":\"1421bda4-d552-49fd-b9bd-edac47a7faf9\",\"type\":\"Toolbar\"},\"toolbar_location\":null,\"x_range\":{\"id\":\"30bde34d-595e-4b63-adf0-0a0cad2b9c84\",\"type\":\"DataRange1d\"},\"y_range\":{\"id\":\"bb0e7510-e60e-40d2-bbcb-b466027f8a04\",\"type\":\"DataRange1d\"}},\"id\":\"6530201a-1af7-47fa-ba27-fad3748f71ac\",\"subtype\":\"Figure\",\"type\":\"Plot\"},{\"attributes\":{\"formatter\":{\"id\":\"4f4a0ca8-ea20-4bf4-8e49-570cae2c7c61\",\"type\":\"BasicTickFormatter\"},\"plot\":{\"id\":\"6530201a-1af7-47fa-ba27-fad3748f71ac\",\"subtype\":\"Figure\",\"type\":\"Plot\"},\"ticker\":{\"id\":\"0b392046-29a9-4cbf-81d4-7a5566b3fc1d\",\"type\":\"BasicTicker\"}},\"id\":\"b454a249-75b8-4669-be8e-9e45bb8defe0\",\"type\":\"LinearAxis\"},{\"attributes\":{\"callback\":null},\"id\":\"30bde34d-595e-4b63-adf0-0a0cad2b9c84\",\"type\":\"DataRange1d\"},{\"attributes\":{\"line_alpha\":{\"value\":0.6},\"line_color\":{\"value\":\"olive\"},\"line_width\":{\"value\":3},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"c87c4965-9ad7-4469-a9fb-d97f92ababc0\",\"type\":\"Segment\"}],\"root_ids\":[\"6530201a-1af7-47fa-ba27-fad3748f71ac\"]},\"title\":\"Bokeh Application\",\"version\":\"0.12.4\"}};\n",
       "            var render_items = [{\"docid\":\"c2fc1c92-22fb-4307-b8ff-1027d3ad8841\",\"elementid\":\"99ab87aa-696e-4cb6-ab89-f6bba1220db3\",\"modelid\":\"6530201a-1af7-47fa-ba27-fad3748f71ac\"}];\n",
       "            \n",
       "            Bokeh.embed.embed_items(docs_json, render_items);\n",
       "          };\n",
       "          if (document.readyState != \"loading\") fn();\n",
       "          else document.addEventListener(\"DOMContentLoaded\", fn);\n",
       "        })();\n",
       "      },\n",
       "      function(Bokeh) {\n",
       "      }\n",
       "    ];\n",
       "  \n",
       "    function run_inline_js() {\n",
       "      \n",
       "      if ((window.Bokeh !== undefined) || (force === true)) {\n",
       "        for (var i = 0; i < inline_js.length; i++) {\n",
       "          inline_js[i](window.Bokeh);\n",
       "        }if (force === true) {\n",
       "          display_loaded();\n",
       "        }} else if (Date.now() < window._bokeh_timeout) {\n",
       "        setTimeout(run_inline_js, 100);\n",
       "      } else if (!window._bokeh_failed_load) {\n",
       "        console.log(\"Bokeh: BokehJS failed to load within specified timeout.\");\n",
       "        window._bokeh_failed_load = true;\n",
       "      } else if (force !== true) {\n",
       "        var cell = $(document.getElementById(\"99ab87aa-696e-4cb6-ab89-f6bba1220db3\")).parents('.cell').data().cell;\n",
       "        cell.output_area.append_execute_result(NB_LOAD_WARNING)\n",
       "      }\n",
       "  \n",
       "    }\n",
       "  \n",
       "    if (window._bokeh_is_loading === 0) {\n",
       "      console.log(\"Bokeh: BokehJS loaded, going straight to plotting\");\n",
       "      run_inline_js();\n",
       "    } else {\n",
       "      load_libs(js_urls, function() {\n",
       "        console.log(\"Bokeh: BokehJS plotting callback run at\", now());\n",
       "        run_inline_js();\n",
       "      });\n",
       "    }\n",
       "  }(this));\n",
       "</script>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
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
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}