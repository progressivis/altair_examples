import io

import pytest

from altair_examples import iter_examples, exec_example
import altair as alt


@pytest.fixture
def require_altair_saver_png():
    try:
        import altair_saver  # noqa: F401
    except ImportError:
        pytest.skip("altair_saver not importable; cannot run saver tests")
    if "png" not in altair_saver.available_formats("vega-lite"):
        pytest.skip("altair_saver not configured to save to png")


@pytest.mark.parametrize("example", iter_examples())
def test_examples(example: dict):
    filename = example["name"] + ".py"
    chart = exec_example(example)

    if chart is None:
        raise ValueError(
            f"Example file {filename} should define chart in its final statement."
        )
    alt.data_transformers.disable_max_rows()
    chart.to_dict()


@pytest.mark.parametrize("example", iter_examples())
def test_render_examples_to_png(require_altair_saver_png, example):
    chart = exec_example(example)

    out = io.BytesIO()
    alt.data_transformers.disable_max_rows()
    chart.save(out, format="png")
    assert out.getvalue().startswith(b"\x89PNG")
