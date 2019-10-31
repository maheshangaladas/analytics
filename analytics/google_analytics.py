"""
analytics.google_analytics
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

import pandas as pd

from analytics.utils import flatten


@flatten
def ga_list_account_summaries(service) -> pd.DataFrame:
    account_summaries = (
        service.management().accountSummaries().list().execute()["items"]
    )
    return account_summaries


@flatten
def ga_list_accounts(service) -> pd.DataFrame:
    accounts = service.management().accounts().list().execute()["items"]
    return accounts


@flatten
def ga_list_webproperties(service, account_id: str) -> pd.DataFrame:
    properties = (
        service.management()
        .webproperties()
        .list(accountId=account_id)
        .execute()["items"]
    )
    return properties


@flatten
def ga_list_account_users(service, account_path: str) -> pd.DataFrame:
    account_users = (
        service.management()
        .accountUserLinks()
        .list(accountId=account_path)
        .execute()["items"]
    )
    return account_users


@flatten
def ga_adwords_links(
    service, account_id: str, webproperty_id: str
) -> pd.DataFrame:
    adwords_links = (
        service.management()
        .webPropertyAdWordsLinks()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()["items"]
    )
    return adwords_links


@flatten
def ga_list_custom_dimensions(
    service, account_id: str, webproperty_id: str
) -> pd.DataFrame:
    custom_dimensions = (
        service.management()
        .customDimensions()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()["items"]
    )
    return custom_dimensions


@flatten
def ga_list_custom_metrics(
    service, account_id: str, webproperty_id: str
) -> pd.DataFrame:
    custom_metrics = (
        service.management()
        .customMetrics()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()["items"]
    )
    return custom_metrics


@flatten
def ga_list_filters(service, account_id: str) -> pd.DataFrame:
    filters = (
        service.management()
        .filters()
        .list(accountId=account_id)
        .execute()["items"]
    )
    return filters


@flatten
def ga_list_views(
    service, account_id: str, webproperty_id: str
) -> pd.DataFrame:
    views = (
        service.management()
        .profiles()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()["items"]
    )
    return views


@flatten
def ga_list_goals(
    service, account_id: str, webproperty_id: str, view_id: str
) -> pd.DataFrame:
    goals = (
        service.management()
        .goals()
        .list(
            accountId=account_id,
            webPropertyId=webproperty_id,
            profileId=view_id,
        )
        .execute()["items"]
    )
    return goals


@flatten
def ga_list_remarketing_audiences(
    service, account_id: str, webproperty_id: str
) -> pd.DataFrame:
    remarketing_audiences = (
        service.management()
        .remarketingAudience()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()["items"]
    )
    return remarketing_audiences


@flatten
def ga_list_segments(service) -> pd.DataFrame:
    segments = service.management().segments().list().execute()["items"]
    return segments
