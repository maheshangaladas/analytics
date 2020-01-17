"""
analytics.search_console
........................

query the google search console API

ref. https://trevorfox.com/2018/03/google-search-console-api-python-tutorial/
"""


from dataclasses import dataclass
from typing import Dict

from googleapiclient.discovery import Resource


@dataclass
class GSCUser(object):
    service: object

    def accounts(self: Resource) -> Dict:
        """retrieve google search console accounts"""
        pass
