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
import googleapiclient
from googleapiclient.discovery import build
from oauth2client import client, file, tools
from oauth2client.service_account import ServiceAccountCredentials

from analytics.scopes import *
from dataclasses import dataclass


@dataclass
class Service(object):
    api_name: str
    api_version: str
    gcp_file: str
    method: str = "client_secret"

    def authenticate(self: object) -> googleapiclient.discovery.Resource:
        """
        obtain a googleapiclient.discovery.Resource object to access google's apis:
        if using service account, give permissions to your service account email in you apps
        to login with a different account, delete the token and re-run the browser authentication flow
        the token is saved in your current project's root directory, if you move it, the authorization won't work

        # TO-DO : improve token storage and retrieval to be location agnostic
        """

        if self.api_name == "tagmanager":
            scopes = GOOGLE_TAG_MANAGER_SCOPES
        elif self.api_name == "analytics":
            scopes = GOOGLE_ANALYTICS_SCOPES
        elif self.api_name == "analyticsreporting":
            scopes = GOOGLE_ANALYTICS_SCOPES
        elif self.api_name == "searchconsole":
            scopes = SEARCH_CONSOLE_SCOPES

        if self.method == "service_account":
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                self.gcp_file, scopes
            )
            service = build(
                self.api_name, self.api_version, credentials=credentials
            )
        elif self.method == "client_secret":
            flow = client.flow_from_clientsecrets(self.gcp_file, scopes)
            storage = file.Storage(self.api_name + "_token.dat")
            credentials = storage.get()
            if credentials is None or credentials.invalid:
                credentials = tools.run_flow(flow, storage)
            http = credentials.authorize(httplib2.Http())
            service = build(self.api_name, self.api_version, http)

        return service
