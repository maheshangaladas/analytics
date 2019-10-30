"""
google.google_analytics
.......................

functions to query the google analytics API

ref. https://www.twilio.com/blog/2018/03/google-analytics-slack-bot-python.html
ref. https://developers.google.com/analytics/devguides/reporting/core/v4/basics
ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference
ref. https://stackoverflow.com/questions/43477702/google-analytics-api-into-csv
ref. https://developers.google.com/analytics/devguides/reporting/core/v4/rest/v4/reports/batchGet
ref. https://code.markedmondson.me/anti-sampling-google-analytics-api/
ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/unsampled-reports
"""

import json
import re
from typing import List, Optional

import pandas as pd
from pandas.io.json import json_normalize

from analytics.utils import clean_names


def ga_list_account_summaries(service) -> pd.DataFrame:
    account_summaries = service.management().accountSummaries().list().execute()
    account_summaries = json_normalize(account_summaries, record_path=["items", "webProperties", "profiles"])
    account_summaries = clean_names(account_summaries)
    return account_summaries


def ga_list_accounts(service) -> pd.DataFrame:
    accounts = service.management().accounts().list().execute()
    accounts = json_normalize(accounts, record_path="items")
    accounts = clean_names(accounts)
    return accounts


def ga_list_webproperties(service, account_id: str) -> pd.DataFrame:
    properties = service.management().webproperties().list(accountId=account_id).execute()
    properties = json_normalize(properties, record_path="items")
    properties = clean_names(properties)
    return properties


def ga_list_account_users(service, account_path: str) -> pd.DataFrame:
    account_users = service.management().accountUserLinks().list(accountId=account_path).execute()
    account_users = json_normalize(account_users, record_path="items")
    account_users = clean_names(account_users)
    return account_users


def ga_adwords_links(service, account_id: str, webproperty_id: str) -> pd.DataFrame:
    adwords_links = service.management().webPropertyAdWordsLinks().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    adwords_links = json_normalize(adwords_links, record_path=["items", "adWordsAccounts"])
    adwords_links = clean_names(adwords_links)
    return adwords_links


def ga_list_custom_dimensions(service, account_id: str, webproperty_id: str) -> pd.DataFrame:
    custom_dimensions = service.management().customDimensions().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    custom_dimensions = json_normalize(custom_dimensions, record_path="items")
    custom_dimensions = clean_names(custom_dimensions)
    return custom_dimensions


def ga_list_custom_metrics(service, account_id: str, webproperty_id: str) -> pd.DataFrame:
    custom_metrics = service.management().customMetrics().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    custom_metrics = json_normalize(custom_metrics, record_path="items")
    custom_metrics = clean_names(custom_metrics)
    return custom_metrics


def ga_list_filters(service, account_id: str) -> pd.DataFrame:
    filters = service.management().filters().list(accountId=account_id).execute()
    filters = json_normalize(filters, record_path="items")
    filters = clean_names(filters)
    return filters


def ga_list_views(service, account_id: str, webproperty_id: str) -> pd.DataFrame:
    views = service.management().profiles().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    views = json_normalize(views, record_path="items")
    views = clean_names(views)
    return views


def ga_list_goals(service, account_id: str, webproperty_id: str, view_id: str) -> pd.DataFrame:
    goals = service.management().goals().list(accountId=account_id, webPropertyId=webproperty_id, profileId=view_id).execute()
    goals = json_normalize(goals, record_path="items")
    goals = clean_names(goals)
    return goals


def ga_list_remarketing_audiences(service, account_id: str, webproperty_id: str) -> pd.DataFrame:
    remarketing_audiences = service.management().remarketingAudience().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    remarketing_audiences = json_normalize(remarketing_audiences, record_path="items")
    remarketing_audiences = clean_names(remarketing_audiences)
    return remarketing_audiences


def ga_list_segments(service) -> pd.DataFrame:
    segments = service.management().segments().list().execute()
    segments = json_normalize(segments, record_path="items")
    segments = clean_names(segments)
    return segments
