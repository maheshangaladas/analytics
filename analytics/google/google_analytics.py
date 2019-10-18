"""
google.google_analytics
.......................

functions to query the google analytics API

# ref. https://www.twilio.com/blog/2018/03/google-analytics-slack-bot-python.html
# ref. https://developers.google.com/analytics/devguides/reporting/core/v4/basics
# ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference
# ref. https://stackoverflow.com/questions/43477702/google-analytics-api-into-csv
# ref. https://developers.google.com/analytics/devguides/reporting/core/v4/rest/v4/reports/batchGet
# ref. https://code.markedmondson.me/anti-sampling-google-analytics-api/
# ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/unsampled-reports
"""

from pandas.io.json import json_normalize
import json
import pandas as pd
from pprint import pprint
import re
from typing import List, Optional


def ga_list_account_summaries(service) -> pd.DataFrame:
    account_summaries = service.management().accountSummaries().list().execute()
    account_summaries = json_normalize(account_summaries, record_path=["items", "webProperties", "profiles"])
    return account_summaries


def ga_list_accounts(service) -> pd.DataFrame:
    accounts = service.management().accounts().list().execute()
    accounts = json_normalize(accounts, record_path="items")
    return accounts


def ga_list_webproperties(service, account_id) -> pd.DataFrame:
    properties = service.management().webproperties().list(accountId=account_id).execute()
    properties = json_normalize(properties, record_path="items")
    return properties


def ga_list_account_users(service, account_path) -> pd.DataFrame:
    account_users = service.management().accountUserLinks().list(accountId=account_path).execute()
    account_users = json_normalize(account_users, record_path="items")
    return account_users


def ga_adwords_links(service, account_id, webproperty_id) -> pd.DataFrame:
    adowrds_links = service.management().webPropertyAdWordsLinks().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    adowrds_links = json_normalize(adowrds_links, record_path="items")
    return adowrds_links


def ga_list_custom_dimensions(service, account_id, webproperty_id) -> pd.DataFrame:
    custom_dimensions = service.management().customDimensions().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    custom_dimensions = json_normalize(custom_dimensions, record_path="items")
    return custom_dimensions


def ga_list_custom_metrics(service, account_id, webproperty_id) -> pd.DataFrame:
    custom_metrics = service.management().customMetrics().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    custom_metrics = json_normalize(custom_metrics, record_path="items")
    return custom_metrics


def ga_list_filters(service, account_id) -> pd.DataFrame:
    filters = service.management().filters().list(accountId=account_id).execute()
    filters = json_normalize(filters, record_path="items")
    return filters


def ga_list_views(service, account_id, webproperty_id) -> pd.DataFrame:
    views = service.management().profiles().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    views = json_normalize(views, record_path="items")
    return views


def ga_list_goals(service, account_id, webproperty_id, view_id) -> pd.DataFrame:
    goals = service.management().goals().list(accountId=account_id, webPropertyId=webproperty_id, profileId=view_id).execute()
    goals = json_normalize(goals, record_path="items")
    return goals


def ga_list_remarketing_audiences(service, account_id, webproperty_id) -> pd.DataFrame:
    remarketing_audiences = service.management().remarketingAudience().list(accountId=account_id, webPropertyId=webproperty_id).execute()
    remarketing_audiences = json_normalize(remarketing_audiences, record_path="items")
    return remarketing_audiences


def ga_list_segments(service) -> pd.DataFrame:
    segments = service.management().segments().list().execute()
    segments = json_normalize(segments, record_path="items")
    return segments


def ga_query(
    service,
    view_id: str,
    startdate: str,
    enddate: str,
    metrics: List[str],
    dimensions: List[str] = None,
    dim_filters: Optional[List[str]] = None,
    met_filters: Optional[List[str]] = None,
):

    #! fix sampling
    #! fix filters
    #! fix mypy Item None
    #! check the logic of what's optional and what's not in the API

    if dim_filters == None and met_filters == None:
        response = (
            service.reports()
            .batchGet(
                body={
                    "reportRequests": [
                        {
                            "viewId": view_id,
                            "dateRanges": [{"startDate": startdate, "endDate": enddate}],
                            "metrics": [{"expression": i} for i in metrics],
                            # "dimensions": [{"name": j} for j in dimensions],
                        }
                    ]
                }
            )
            .execute()
        )
    else:
        response = pd.DataFrame()

    result = parse_response(response)
    return result


def parse_response(response: pd.DataFrame) -> pd.DataFrame:
    reports = response["reports"][0]
    column_header = reports["columnHeader"]["dimensions"]
    metric_header = reports["columnHeader"]["metricHeader"]["metricHeaderEntries"]

    columns = column_header
    for metric in metric_header:
        columns.append(metric["name"])

    columns = [re.sub("(.)([A-Z][a-z]+)", r"\1_\2", w).lower() for w in columns]
    columns = [re.sub(":", "_", w) for w in columns]

    data = json_normalize(reports["data"]["rows"])
    data_dimensions = pd.DataFrame(data["dimensions"].tolist())
    data_metrics = pd.DataFrame(data["metrics"].tolist())
    data_metrics = data_metrics.applymap(lambda x: x["values"])
    data_metrics = pd.DataFrame(data_metrics[0].tolist())
    result = pd.concat([data_dimensions, data_metrics], axis=1, ignore_index=True)

    result.columns = columns
    return result
