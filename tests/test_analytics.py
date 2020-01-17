"""
tests
.....

testing analytics functions
"""


import googleapiclient

from analytics.authorization import Service
from analytics.google_analytics import GAUser
from analytics.google_tag_manager import GTMUser
from analytics.page_insights import URL
from analytics.utm_tags import utm_tag

gcp_client = "gcp-client.json"

accountpath = "accounts/4703034098"
containerpath = "accounts/4703034098/containers/13195950"
workspacepath = "accounts/4703034098/containers/13195265/workspaces/5"

accountid = "3100168"
propertyid = "UA-3100168-49"
viewid = "169728486"


def test_seo():
    testurl = "https://www.hemnet.se"
    url = URL(testurl)
    url.inspect()
    assert isinstance(url, URL)
    assert url.attributes is not None
    assert url.attributes["status_code"] == 200


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


def test_utm_tags():
    good_url = "https://www.google.com/"
    alternative_url = "https://www.emailservice.com"
    source = "google"
    alternative_source = "newsletter"
    medium = "cpc"
    alternative_medium = "email"
    name = "spring_sale"
    alternative_name = "fall_sale"
    alternative_term = "running_shoes"
    alternative_content = "email_banner"

    google_tag = utm_tag(good_url, source, medium, name)
    email_tag = utm_tag(
        alternative_url,
        alternative_source,
        alternative_medium,
        alternative_name,
        alternative_term,
        alternative_content,
    )

    correct_google_utm = "https://www.google.com/?utm_source=google&utm_medium=cpc&utm_campaign=spring_sale"
    correct_email_utm = "https://www.emailservice.com/?utm_source=newsletter&utm_medium=email&utm_campaign=fall_sale&utm_term=running_shoes&utm_content=email_banner"

    assert google_tag == correct_google_utm
    assert email_tag == correct_email_utm
