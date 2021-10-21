"""
Simple Histogram
----------------
This example shows how to make a basic histogram, based on the vega-lite docs
https://vega.github.io/vega-lite/examples/histogram.html
"""
# category: simple charts
import altair as alt
from vega_datasets import data
from altair_examples import fix_columns

source = data.movies()
fix_columns(source)

(
    alt.Chart(source)
    .mark_bar()
    .encode(alt.X("IMDB_Rating:Q", bin=True), y="count()",)
)
