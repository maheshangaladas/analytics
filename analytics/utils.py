"""
analytics.utils
...............

utility functions
"""

import pandas as pd
import re


def clean_names(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset.columns = [re.sub("(.)([A-Z][a-z]+)", r"\1_\2", w).lower() for w in dataset.columns]
    dataset.columns = [re.sub(":", "_", w) for w in dataset.columns]
    dataset.columns = [re.sub(r"\.", "_", w) for w in dataset.columns]
    return dataset


def explode_columns():
    # want to explode columns with lists of dictionaries (t.ex user permissions in GTM has containerAccess column)
    pass
