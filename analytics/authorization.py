"""
analytics.auth
...........

authorization logic for google APIs.

ref. https://developers.google.com/apis-explorer/#p/ (services)
ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/quickstart/service-py (service account authorization)
ref. https://developers.google.com/identity/protocols/googlescopes (API scopes)
ref. https://developers.google.com/tag-manager/api/v1/devguide (client authorization)
"""

import httplib2
from googleapiclient.discovery import build
from oauth2client import client, file, tools
from oauth2client.service_account import ServiceAccountCredentials

from analytics.scopes import *


def get_service(api_name, api_version, gcp_file, method="client_secret"):
    """
    obtain service object to access google's apis:
    - for service account authorization, remember to give permissions to your service account email in you apps
    - to login with a different account, just delete the token and re-run the flow
    - the token gets saved in your current project's root directory, if you move it, the authorization won't work
    (this function needs some improvements to handle token storage and retrieval yet)
    """
    if api_name == "tagmanager":
        scopes = GOOGLE_TAG_MANAGER_SCOPES
    elif api_name == "analytics":
        scopes = GOOGLE_ANALYTICS_SCOPES
    elif api_name == "analyticsreporting":
        scopes = GOOGLE_ANALYTICS_SCOPES
    elif api_name == "searchconsole":
        scopes = SEARCH_CONSOLE_SCOPES

    if method == "service_account":
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            gcp_file, scopes
        )
        service = build(api_name, api_version, credentials=credentials)
    elif method == "client_secret":
        flow = client.flow_from_clientsecrets(gcp_file, scopes)
        storage = file.Storage(api_name + "_token.dat")
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(httplib2.Http())
        service = build(api_name, api_version, http)

    return service
