"""
Simple Line Chart
-----------------
This chart shows the most basic line chart, made from a dataframe with two
columns.
"""
# category: simple charts

import altair as alt
import numpy as np

x = np.arange(100)
source = alt.pd.DataFrame({"x": x, "f(x)": np.sin(x / 5)})

alt.Chart(source).mark_line().encode(x="x", y="f(x)")
