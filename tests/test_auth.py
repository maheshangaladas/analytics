"""
tests.google
............

testing google API functions
"""

from analytics.authorization import get_service
import googleapiclient


# gcp_client = "/Users/wnguessan/gcp-client.json"
gcp_client = "gcp-client.json.enc"
gtmservice = get_service("tagmanager", "v2", gcp_client)


def test_gtm_authorization():
    gtmservice = get_service("tagmanager", "v2", gcp_client)
    assert isinstance(gtmservice, googleapiclient.discovery.Resource)


def test_ga_authorization():
    pass
