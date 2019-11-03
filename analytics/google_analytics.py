"""
analytics.google_analytics
..........................

functions to query the google analytics API

ref. https://www.twilio.com/blog/2018/03/google-analytics-slack-bot-python.html
ref. https://developers.google.com/analytics/devguides/reporting/core/v4/basics
ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference
ref. https://stackoverflow.com/questions/43477702/google-analytics-api-into-csv
ref. https://developers.google.com/analytics/devguides/reporting/core/v4/rest/v4/reports/batchGet
ref. https://code.markedmondson.me/anti-sampling-google-analytics-api/
ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/unsampled-reports
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class GAUser(object):
    service: object

    def summaries(self) -> Dict:
        summaries = (
            self.service.management().accountSummaries().list().execute()
        )
        return summaries

    def accounts(self) -> Dict:
        accounts = self.service.management().accounts().list().execute()
        return accounts

    def properties(self, account_id: str) -> Dict:
        properties = (
            self.service.management()
            .webproperties()
            .list(accountId=account_id)
            .execute()
        )
        return properties

    def users(self, account_id: str) -> Dict:
        users = (
            self.service.management()
            .accountUserLinks()
            .list(accountId=account_id)
            .execute()
        )
        return users

    def adwords_links(self, account_id: str, property_id: str) -> Dict:
        adwords_links = (
            self.service.management()
            .webPropertyAdWordsLinks()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return adwords_links

    def custom_dimensions(self, account_id: str, property_id: str) -> Dict:
        custom_dimensions = (
            self.service.management()
            .customDimensions()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return custom_dimensions

    def custom_metrics(self, account_id: str, property_id: str) -> Dict:
        custom_metrics = (
            self.service.management()
            .customMetrics()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return custom_metrics

    def filters(self, account_id: str) -> Dict:
        filters = (
            self.service.management()
            .filters()
            .list(accountId=account_id)
            .execute()
        )
        return filters

    def views(self, account_id: str, property_id: str) -> Dict:
        views = (
            self.service.management()
            .profiles()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return views

    def goals(self, account_id: str, property_id: str, view_id: str) -> Dict:
        goals = (
            self.service.management()
            .goals()
            .list(
                accountId=account_id,
                webPropertyId=property_id,
                profileId=view_id,
            )
            .execute()
        )
        return goals

    def remarketing(self, account_id: str, property_id: str) -> Dict:
        remarketing_audiences = (
            self.service.management()
            .remarketingAudience()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return remarketing_audiences

    def segments(self) -> Dict:
        segments = self.service.management().segments().list().execute()
        return segments
