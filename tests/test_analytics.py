"""
tests.test_gtm
..............

testing google tag manager api functions
"""

import os

import googleapiclient
import pandas as pd

from analytics.authorization import get_service
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


def test_google_tag_manager():
    # gcp_client = os.environ["gcp_client_path"] # for local testing

    gcp_client = "gcp-client.json.enc"

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
