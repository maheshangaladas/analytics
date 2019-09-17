"""
google.auth
...........

authorization logic for google APIs.
"""

from googleapiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials
from analytics.google.scopes import *


def get_service(api_name, api_version, record, method="service_account"):
    """Obtain service to use to interact with Google API. This solution is cobbled together from a variety of sources.
    Google has deprecated parts of its libraries but hasn't updated its documentation.

    ref. https://developers.google.com/apis-explorer/#p/ (services)
    ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/quickstart/service-py (service account authorization)
    ref. https://developers.google.com/identity/protocols/googlescopes (API scopes)
    ref. https://developers.google.com/tag-manager/api/v1/devguide (client authorization)

    Note! On Google Cloud Platform, a service account is linked to an email. 
    For service account authorization to work, you must give permissions to your service account email in your various applications.
    
    :param api_name: name of the api
    :type api_name: str
    :param api_version: version of the api
    :type api_version: str
    :param record: service account or client secret JSON file(s)
    :type record: str
    :param method: type of authentication (service_account or client_secret), defaults to "service_account"
    :type method: str, optional
    :return: service object
    :rtype: googleapiclient.discovery.Resource
    """
    if api_name == "tagmanager":
        scopes = GOOGLE_TAG_MANAGER_SCOPES
    elif api_name == "analytics":
        scopes = GOOGLE_ANALYTICS_SCOPES
    elif api_name == "searchconsole":
        scopes = SEARCH_CONSOLE_SCOPES

    if method == "service_account":
        credentials = ServiceAccountCredentials.from_json_keyfile_name(record, scopes)
        service = build(api_name, api_version, credentials=credentials)
    elif method == "client_secret":
        flow = client.flow_from_clientsecrets(record, scopes)
        storage = file.Storage(api_name + "_token.dat")
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(httplib2.Http())
        service = build(api_name, api_version, http)

    return service

