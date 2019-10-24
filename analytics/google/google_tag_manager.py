"""
google.google_tag_manager
.........................

functions to query the google tag manager API

ref. https://developers.google.com/tag-manager/api/v2/devguide
"""

from pandas.io.json import json_normalize
import pandas as pd
from analytics.google.utils import clean_names


def gtm_list_accounts(service) -> pd.DataFrame:
    accounts = service.accounts().list().execute()
    accounts = json_normalize(accounts, record_path="account")
    accounts = clean_names(accounts)
    return accounts


def gtm_list_permissions(service, account_path: str) -> pd.DataFrame:
    permissions = service.accounts().user_permissions().list(parent=account_path).execute()
    permissions = json_normalize(permissions, record_path="userPermission")
    permissions = clean_names(permissions)
    return permissions


def gtm_list_containers(service, account_path: str) -> pd.DataFrame:
    containers = service.accounts().containers().list(parent=account_path).execute()
    containers = json_normalize(containers, record_path="container")
    containers = clean_names(containers)
    return containers


def gtm_list_workspaces(service, container_path: str) -> pd.DataFrame:
    workspaces = service.accounts().containers().workspaces().list(parent=container_path).execute()
    workspaces = json_normalize(workspaces, record_path="workspace")
    workspaces = clean_names(workspaces)
    return workspaces


def gtm_list_environments(service, container_path: str) -> pd.DataFrame:
    environments = service.accounts().containers().environments().list(parent=container_path).execute()
    environments = json_normalize(environments, record_path="environment")
    environments = clean_names(environments)
    return environments


def gtm_list_variables(service, workspace_path: str) -> pd.DataFrame:
    variables = service.accounts().containers().workspaces().variables().list(parent=workspace_path).execute()
    variables = json_normalize(variables, record_path="variable")
    variables = clean_names(variables)
    return variables


def gtm_list_tags(service, workspace_path: str) -> pd.DataFrame:
    tags = service.accounts().containers().workspaces().tags().list(parent=workspace_path).execute()
    tags = json_normalize(tags, record_path="tag")
    tags = clean_names(tags)
    return tags


def gtm_list_triggers(service, workspace_path: str) -> pd.DataFrame:
    triggers = service.accounts().containers().workspaces().triggers().list(parent=workspace_path).execute()
    triggers = json_normalize(triggers, record_path="trigger")
    triggers = clean_names(triggers)
    return triggers
