"""
analytics.search_console
........................

query the google search console API
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
