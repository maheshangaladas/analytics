# this should become OOP to avoid repetitions and shit like that
# futhermore, I gotta figure out what I actually want it to return

from pprint import pprint

import googleapiclient

from analytics.google_products.authorization import Service
from analytics.google_products.google_tag_manager import GTMUser


def gtm_auth(client: str) -> googleapiclient.discovery.Resource:
    """authorize into the google tag manager API"""
    service = Service("tagmanager", "v2", client).authenticate()
    ga_user = GTMUser(service)
    return ga_user


def accounts_collection(user, account_ids):
    """return selected accounts"""
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    return selected_accounts


def permissions_collection(user, account_ids):
    """return permissions for selected accounts"""
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    account_paths = [i["path"] for i in selected_accounts]
    permissions = [
        user.permissions(i)["userPermission"] for i in account_paths
    ]
    return permissions


def containers_collection(user, account_ids):
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    account_paths = [i["path"] for i in selected_accounts]
    containers = [user.containers(i)["container"] for i in account_paths]
    return containers


def workspaces_collection(user, account_ids):
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    account_paths = [i["path"] for i in selected_accounts]
    containers = [user.containers(i)["container"] for i in account_paths]
    container_paths = [j["path"] for i in containers for j in i]
    workspaces = [user.workspaces(i)["workspace"] for i in container_paths]
    return workspaces


def environments_collection(user, account_ids):
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    account_paths = [i["path"] for i in selected_accounts]
    containers = [user.containers(i)["container"] for i in account_paths]
    container_paths = [j["path"] for i in containers for j in i]
    environments = [
        user.environments(i)["environment"] for i in container_paths
    ]
    return environments


def tags_collection(user, account_ids):
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    account_paths = [i["path"] for i in selected_accounts]
    containers = [user.containers(i)["container"] for i in account_paths]
    container_paths = [j["path"] for i in containers for j in i]
    workspaces = [user.workspaces(i)["workspace"] for i in container_paths]
    workspace_paths = [j["path"] for i in workspaces for j in i]
    tags = [user.tags(i)["tag"] for i in workspace_paths]
    return tags


def triggers_collection(user, account_ids):
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    account_paths = [i["path"] for i in selected_accounts]
    containers = [user.containers(i)["container"] for i in account_paths]
    container_paths = [j["path"] for i in containers for j in i]
    workspaces = [user.workspaces(i)["workspace"] for i in container_paths]
    workspace_paths = [j["path"] for i in workspaces for j in i]
    triggers = [user.triggers(i)["trigger"] for i in workspace_paths]
    return triggers


def variables_collection(user, account_ids):
    accounts = user.accounts()["account"]
    selected_accounts = [d for d in accounts if d["accountId"] in account_ids]
    account_paths = [i["path"] for i in selected_accounts]
    containers = [user.containers(i)["container"] for i in account_paths]
    container_paths = [j["path"] for i in containers for j in i]
    workspaces = [user.workspaces(i)["workspace"] for i in container_paths]
    workspace_paths = [j["path"] for i in workspaces for j in i]
    variables = [user.variables(i)["variable"] for i in workspace_paths]
    return variables


if __name__ == "__main__":
    nvv_accounts = ["87114"]
    gcp_client = "gcp-client.json"
    gtm_user = gtm_auth(gcp_client)

    pprint(accounts_collection(gtm_user, nvv_accounts))
    pprint(permissions_collection(gtm_user, nvv_accounts))
    pprint(containers_collection(gtm_user, nvv_accounts))
    pprint(workspaces_collection(gtm_user, nvv_accounts))
    pprint(environments_collection(gtm_user, nvv_accounts))
    pprint(tags_collection(gtm_user, nvv_accounts))
    pprint(triggers_collection(gtm_user, nvv_accounts))
    pprint(variables_collection(gtm_user, nvv_accounts))
