"""
tests.google
............

testing google API functions
"""
from analytics.google.auth import *
from analytics.google.google_tag_manager import *
import pandas as pd

gcp_client = "/Users/wnguessan/gcp-client.json"
gtmservice = get_service("tagmanager", "v2", gcp_client)


def test_gtm_list_accounts():
    response = gtm_list_accounts(gtmservice)
    assert isinstance(response, pd.DataFrame)


def test_gtm_list_permissions():
    pass
