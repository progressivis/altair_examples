"""
Examples of Altair specifications.
"""
import os
from altair.utils.execeval import eval_block


def fix_columns(df):
    """Fix column names, replacing space by underline, for Vega.
    """
    df.columns = [c.replace(" ", "_") for c in df.columns]


def iter_examples():
    """Iterate over the examples in this directory.

    Each item is a dict with the following keys:
    - "name" : the unique name of the example
    - "filename" : the full file path to the example
    """
    example_dir = os.path.abspath(os.path.dirname(__file__))
    for filename in os.listdir(example_dir):
        name, ext = os.path.splitext(filename)
        if name.startswith("_") or ext != ".py":
            continue
        yield {"name": name, "filename": os.path.join(example_dir, filename)}


def exec_example(example):
    """Execute an example return by `iter_examples' and returns the chart.

    Parameters
    ----------
    example: dict
        the example dict should contain the key "filename", as returned by
        `iter_examples`
    """
    with open(example["filename"], "r") as fin:
        code = fin.read()
    return eval_block(code, filename=example["filename"])
