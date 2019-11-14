"""
analytics.google_analytics
..........................

functions to query the google analytics API.

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

from googleapiclient.discovery import Resource


@dataclass
class GAUser(object):
    service: object

    def summaries(self: Resource) -> Dict:
        """retrieve account summaries for a user"""
        summaries = (
            self.service.management().accountSummaries().list().execute()
        )
        return summaries

    def accounts(self: Resource) -> Dict:
        """retrieve accounts for a user"""
        accounts = self.service.management().accounts().list().execute()
        return accounts

    def properties(self: Resource, account_id: str) -> Dict:
        """retrieve properties for an account"""
        properties = (
            self.service.management()
            .webproperties()
            .list(accountId=account_id)
            .execute()
        )
        return properties

    def users(self: Resource, account_id: str) -> Dict:
        """retrieve users for an account"""
        users = (
            self.service.management()
            .accountUserLinks()
            .list(accountId=account_id)
            .execute()
        )
        return users

    def adwords_links(
        self: Resource, account_id: str, property_id: str
    ) -> Dict:
        """retrieve adwords links for a property"""
        adwords_links = (
            self.service.management()
            .webPropertyAdWordsLinks()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return adwords_links

    def custom_dimensions(
        self: Resource, account_id: str, property_id: str
    ) -> Dict:
        """retrieve custom dimensions for a property"""
        custom_dimensions = (
            self.service.management()
            .customDimensions()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return custom_dimensions

    def custom_metrics(
        self: Resource, account_id: str, property_id: str
    ) -> Dict:
        """retrieve custom metrics for a property"""
        custom_metrics = (
            self.service.management()
            .customMetrics()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return custom_metrics

    def filters(self: Resource, account_id: str) -> Dict:
        """retrieve filters for an account"""
        filters = (
            self.service.management()
            .filters()
            .list(accountId=account_id)
            .execute()
        )
        return filters

    def views(self: Resource, account_id: str, property_id: str) -> Dict:
        """retrieve views for a property"""
        views = (
            self.service.management()
            .profiles()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return views

    def goals(
        self: Resource, account_id: str, property_id: str, view_id: str
    ) -> Dict:
        """retrieve goals for a view"""
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

    def remarketing(self: Resource, account_id: str, property_id: str) -> Dict:
        """retrieve remarketing lists for a property"""
        remarketing_audiences = (
            self.service.management()
            .remarketingAudience()
            .list(accountId=account_id, webPropertyId=property_id)
            .execute()
        )
        return remarketing_audiences

    def segments(self: Resource) -> Dict:
        """retrieve segments for an account"""
        segments = self.service.management().segments().list().execute()
        return segments
