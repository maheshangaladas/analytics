"""
google.google_analytics
.......................

functions for the google analytics API.

# ref. https://www.twilio.com/blog/2018/03/google-analytics-slack-bot-python.html
# ref. https://developers.google.com/analytics/devguides/reporting/core/v4/basics
# ref. https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference
"""


def ga_list_account_summaries(service):
    return service.management().accountSummaries().list().execute()


def ga_list_accounts(service):
    return service.management().accounts().list().execute()


def ga_list_webproperties(service, account_id):
    return service.management().webproperties().list(accountId=account_id).execute()


def ga_list_account_users(service, account_path):
    return (
        service.management().accountUserLinks().list(accountId=account_path).execute()
    )


def ga_adwords_links(service, account_id, webproperty_id):
    return (
        service.management()
        .webPropertyAdWordsLinks()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()
    )


def ga_list_custom_dimensions(service, account_id, webproperty_id):
    return (
        service.management()
        .customDimensions()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()
    )


def ga_list_custom_metrics(service, account_id, webproperty_id):
    return (
        service.management()
        .customMetrics()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()
    )


def ga_list_filters(service, account_id):
    return service.management().filters().list(accountId=account_id).execute()


def ga_list_views(service, account_id, webproperty_id):
    return (
        service.management()
        .profiles()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()
    )


def ga_list_goals(service, account_id, webproperty_id, view_id):
    return (
        service.management()
        .goals()
        .list(accountId=account_id, webPropertyId=webproperty_id, profileId=view_id)
        .execute()
    )


def ga_list_remarketing_audiences(service, account_id, webproperty_id):
    return (
        service.management()
        .remarketingAudience()
        .list(accountId=account_id, webPropertyId=webproperty_id)
        .execute()
    )


def ga_list_segments(service):
    return service.management().segments().list().execute()


def ga_query():
    pass

