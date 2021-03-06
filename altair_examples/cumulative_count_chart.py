"""
Cumulative Count Chart
----------------------
This example shows an area chart with cumulative count.
Adapted from https://vega.github.io/vega-lite/examples/area_cumulative_freq.html

"""
# category: area charts

import altair as alt
from vega_datasets import data
from altair_examples import fix_columns

source = data.movies()
fix_columns(source)

(
    alt.Chart(source)
    .transform_window(
        cumulative_count="count()", sort=[{"field": "IMDB_Rating"}],
    )
    .mark_area()
    .encode(x="IMDB_Rating:Q", y="cumulative_count:Q")
)
