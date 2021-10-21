"""
Binned Scatterplot
------------------
This example shows how to make a binned scatterplot.
"""
# category: scatter plots
import altair as alt
from vega_datasets import data
from altair_examples import fix_columns

source = data.movies()
fix_columns(source)

(
    alt.Chart(source)
    .mark_circle()
    .encode(
        alt.X("IMDB_Rating:Q", bin=True),
        alt.Y("Rotten_Tomatoes_Rating:Q", bin=True),
        size="count()",
    )
)
