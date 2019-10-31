"""
google.google_tag_manager
.........................

functions to query the google tag manager API

ref. https://developers.google.com/tag-manager/api/v2/devguide
"""

import pandas as pd

from analytics.utils import flatten


@flatten
def gtm_list_accounts(service) -> pd.DataFrame:
    accounts = service.accounts().list().execute()["account"]
    return accounts


@flatten
def gtm_list_permissions(service, account_path: str) -> pd.DataFrame:
    permissions = (
        service.accounts()
        .user_permissions()
        .list(parent=account_path)
        .execute()["userPermission"]
    )
    return permissions


@flatten
def gtm_list_containers(service, account_path: str) -> pd.DataFrame:
    containers = (
        service.accounts()
        .containers()
        .list(parent=account_path)
        .execute()["container"]
    )
    return containers


@flatten
def gtm_list_workspaces(service, container_path: str) -> pd.DataFrame:
    workspaces = (
        service.accounts()
        .containers()
        .workspaces()
        .list(parent=container_path)
        .execute()["workspace"]
    )
    return workspaces


@flatten
def gtm_list_environments(service, container_path: str) -> pd.DataFrame:
    environments = (
        service.accounts()
        .containers()
        .environments()
        .list(parent=container_path)
        .execute()["environment"]
    )
    return environments


@flatten
def gtm_list_tags(service, workspace_path: str) -> pd.DataFrame:
    tags = (
        service.accounts()
        .containers()
        .workspaces()
        .tags()
        .list(parent=workspace_path)
        .execute()["tag"]
    )
    return tags


@flatten
def gtm_list_variables(service, workspace_path: str) -> pd.DataFrame:
    variables = (
        service.accounts()
        .containers()
        .workspaces()
        .variables()
        .list(parent=workspace_path)
        .execute()["variable"]
    )
    return variables


@flatten
def gtm_list_triggers(service, workspace_path: str) -> pd.DataFrame:
    triggers = (
        service.accounts()
        .containers()
        .workspaces()
        .triggers()
        .list(parent=workspace_path)
        .execute()["trigger"]
    )
    return triggers
