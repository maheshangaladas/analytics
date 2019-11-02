"""
tests
..............

testing analytics functions
"""

import googleapiclient
import pandas as pd

from analytics.authorization import Service
from analytics.google_tag_manager import GTMUser
from analytics.google_analytics import GAUser

gcp_client = "gcp-client.json"

accountpath = "accounts/4703034098"
containerpath = "accounts/4703034098/containers/13195950"
workspacepath = "accounts/4703034098/containers/13195265/workspaces/5"

accountid = "3100168"
propertyid = "UA-3100168-49"
viewid = "169728486"


def test_authorization():
    service = Service("tagmanager", "v2", gcp_client).authenticate()
    assert isinstance(service, googleapiclient.discovery.Resource)


def test_google_tag_manager():
    service = Service("tagmanager", "v2", gcp_client).authenticate()
    user = GTMUser(service)

    accounts = user.accounts()
    assert isinstance(accounts, dict)

    permissions = user.permissions(accountpath)
    assert isinstance(permissions, dict)

    containers = user.containers(accountpath)
    assert isinstance(containers, dict)

    environments = user.environments(containerpath)
    assert isinstance(environments, dict)

    workspaces = user.workspaces(containerpath)
    assert isinstance(workspaces, dict)

    tags = user.tags(workspacepath)
    assert isinstance(tags, dict)

    variables = user.variables(workspacepath)
    assert isinstance(variables, dict)

    triggers = user.triggers(workspacepath)
    assert isinstance(triggers, dict)


def test_google_analytics():
    service = Service("analytics", "v3", gcp_client).authenticate()
    user = GAUser(service)

    summaries = user.summaries()
    assert isinstance(summaries, dict)

    accounts = user.accounts()
    assert isinstance(accounts, dict)

    users = user.users(accountid)
    assert isinstance(users, dict)

    properties = user.properties(accountid)
    assert isinstance(properties, dict)

    adwords = user.adwords_links(accountid, propertyid)
    assert isinstance(adwords, dict)

    dimensions = user.custom_dimensions(accountid, propertyid)
    assert isinstance(dimensions, dict)

    metrics = user.custom_metrics(accountid, propertyid)
    assert isinstance(metrics, dict)

    filters = user.filters(accountid)
    assert isinstance(filters, dict)

    views = user.views(accountid, propertyid)
    assert isinstance(views, dict)

    goals = user.goals(accountid, propertyid, viewid)
    assert isinstance(goals, dict)

    remarketing = user.remarketing(accountid, propertyid)
    assert isinstance(remarketing, dict)

    segments = user.segments()
    assert isinstance(segments, dict)

