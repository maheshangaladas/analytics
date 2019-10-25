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
from analytics.scopes import *


def get_service(api_name, api_version, gcp_file, method="client_secret"):
    """Obtain service to use to interact with Google API. This solution is cobbled together from a variety of sources.
    Google has deprecated parts of its libraries but hasn't updated its documentation.

    ref. https://developers.google.com/apis-explorer/#p/ (services)
    ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/quickstart/service-py (service account authorization)
    ref. https://developers.google.com/identity/protocols/googlescopes (API scopes)
    ref. https://developers.google.com/tag-manager/api/v1/devguide (client authorization)

    Note! On Google Cloud Platform, a service account is linked to an email. 
    For service account authorization to work, you must give permissions to your service account email in your various applications.
    
    Note! If you want to log in with a different account, then remove the .dat token file from your machine. 
    to authenticate as new user just delete the tokens that are saved on your computer
    #! what happens if you move the token?? what happens if you want to save it somewhere else? how does the library finds it?
    #! if you change the file location get_service won't find it (so you need to keep it where it's at)
    :param api_name: name of the api
    :type api_name: str
    :param api_version: version of the api
    :type api_version: str
    :param filepath: service account or client secret JSON file(s)
    :type filepath: str
    :param method: type of authentication (service_account or client_secret), defaults to "service_account"
    :type method: str, optional
    :return: service object
    :rtype: googleapiclient.discovery.Resource
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
        credentials = ServiceAccountCredentials.from_json_keyfile_name(gcp_file, scopes)
        service = build(api_name, api_version, credentials=credentials)
    elif method == "client_secret":
        flow = client.flow_from_clientsecrets(gcp_file, scopes)
        storage = file.Storage(api_name + "_token.dat")  #! change here to set where the token should be saved (and logic to retrive it)
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(httplib2.Http())
        service = build(api_name, api_version, http)

    return service

