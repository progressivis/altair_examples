"""
Layered Histogram
=================
This example shows how to use opacity to make a layered histogram in Altair.
"""
# category: histograms
import altair as alt
import numpy as np

np.random.seed(42)

# Generating Data
source = alt.pd.DataFrame(
    {
        "Trial A": np.random.normal(0, 0.8, 1000),
        "Trial B": np.random.normal(-2, 1, 1000),
        "Trial C": np.random.normal(3, 2, 1000),
    }
)

(
    alt.Chart(source)
    .transform_fold(
        ["Trial A", "Trial B", "Trial C"], as_=["Experiment", "Measurement"]
    )
    .mark_area(opacity=0.3, interpolate="step")
    .encode(
        alt.X("Measurement:Q", bin=alt.Bin(maxbins=100)),
        alt.Y("count()", stack=None),
        alt.Color("Experiment:N"),
    )
)
