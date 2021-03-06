"""
Binned Heatmap
--------------
This example shows how to make a heatmap from binned quantitative data.
"""
# category: other charts
import altair as alt
from vega_datasets import data
from altair_examples import fix_columns

source = data.movies()
fix_columns(source)

(
    alt.Chart(source)
    .mark_rect()
    .encode(
        alt.X("IMDB_Rating:Q", bin=alt.Bin(maxbins=60)),
        alt.Y("Rotten_Tomatoes_Rating:Q", bin=alt.Bin(maxbins=40)),
        alt.Color("count():Q", scale=alt.Scale(scheme="greenblue")),
    )
)
