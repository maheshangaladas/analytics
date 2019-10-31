"""
analytics.utils
...............

utility functions

ref. ref. https://stackoverflow.com/questions/52795561/flattening-nested-json-in-pandas-data-frame
"""

import pandas as pd
import re
from pandas.io.json import json_normalize
from typing import List, Callable, Dict
from inflection import underscore
import functools


def _unnest(response: List, exclude=[""]) -> Dict:
    out = dict()

    def _extract(record, name="", exclude=exclude):
        if type(record) is dict:
            for key in record:
                if key not in exclude:
                    _extract(record[key], name + key + "_")
        elif type(record) is list:
            i = 0
            for item in record:
                _extract(item, name + str(i) + "_")
                i += 1
        else:
            out[name[:-1]] = record

    _extract(response)
    return out


def flatten(func: Callable) -> pd.DataFrame:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        response = pd.DataFrame(_unnest(x) for x in response)
        response.columns = [underscore(w) for w in response.columns]
        return response

    return wrapper
