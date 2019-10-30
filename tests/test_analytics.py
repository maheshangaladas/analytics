"""
tests.test_gtm
..............

testing google tag manager api functions
"""

import os

import googleapiclient
import pandas as pd

from analytics.authorization import get_service
from analytics.google_analytics import (
    ga_adwords_links,
    ga_list_account_summaries,
    ga_list_account_users,
    ga_list_accounts,
    ga_list_custom_dimensions,
    ga_list_custom_metrics,
    ga_list_filters,
    ga_list_goals,
    ga_list_remarketing_audiences,
    ga_list_segments,
    ga_list_views,
    ga_list_webproperties,
)
from analytics.google_tag_manager import (
    gtm_list_accounts,
    gtm_list_containers,
    gtm_list_environments,
    gtm_list_permissions,
    gtm_list_tags,
    gtm_list_triggers,
    gtm_list_variables,
    gtm_list_workspaces,
)


gcp_client = "gcp-client.json"


def test_google_tag_manager():

    gtm_service = get_service("tagmanager", "v2", gcp_client)
    assert isinstance(gtm_service, googleapiclient.discovery.Resource)

    accounts = gtm_list_accounts(gtm_service)
    assert isinstance(accounts, pd.DataFrame)

    account = accounts.iloc[0, 0]
    permissions = gtm_list_permissions(gtm_service, account)
    assert isinstance(permissions, pd.DataFrame)

    containers = gtm_list_containers(gtm_service, account)
    assert isinstance(containers, pd.DataFrame)

    container = containers.iloc[0, 0]
    workspaces = gtm_list_workspaces(gtm_service, container)
    assert isinstance(workspaces, pd.DataFrame)

    environments = gtm_list_environments(gtm_service, container)
    assert isinstance(environments, pd.DataFrame)

    workspace = workspaces.iloc[0, 0]
    variables = gtm_list_variables(gtm_service, workspace)
    assert isinstance(variables, pd.DataFrame)

    tags = gtm_list_tags(gtm_service, workspace)
    assert isinstance(tags, pd.DataFrame)

    triggers = gtm_list_triggers(gtm_service, workspace)
    assert isinstance(triggers, pd.DataFrame)


# def test_google_analytics():

#     ga_service = get_service("analytics", "v3", gcp_client)
#     ga_reporting = get_service("analyticsreporting", "v4", gcp_client)

#     summaries = ga_list_account_summaries(ga_service)
#     assert isinstance(summaries, pd.DataFrame)

#     accounts = ga_list_accounts(ga_service)
#     account = accounts.iloc[0, 0]
#     assert isinstance(accounts, pd.DataFrame)

#     properties = ga_list_webproperties(ga_service, account)
#     webprop = properties.iloc[0, 0]
#     assert isinstance(properties, pd.DataFrame)

#     users = ga_list_account_users(ga_service, account)
#     assert isinstance(users, pd.DataFrame)

#     adwords_links = ga_adwords_links(ga_service, account, webprop)
#     assert isinstance(adwords_links, pd.DataFrame)

#     custom_dimensions = ga_list_custom_dimensions(ga_service, account, webprop)
#     assert isinstance(custom_dimensions, pd.DataFrame)

#     custom_metrics = ga_list_custom_metrics(ga_service, account, webprop)
#     assert isinstance(custom_metrics, pd.DataFrame)

#     filters = ga_list_filters(ga_service, account)
#     assert isinstance(filters, pd.DataFrame)

#     views = ga_list_views(ga_service, account, webprop)
#     view = views.iloc[0, 0]
#     assert isinstance(views, pd.DataFrame)

#     goals = ga_list_goals(ga_service, account, webprop, view)
#     assert isinstance(goals, pd.DataFrame)

#     audiences = ga_list_remarketing_audiences(ga_service, account, webprop)
#     assert isinstance(audiences, pd.DataFrame)

#     segments = ga_list_segments(ga_service)
#     assert isinstance(segments, pd.DataFrame)
