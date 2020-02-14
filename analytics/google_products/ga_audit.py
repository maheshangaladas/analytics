from pprint import pprint

import googleapiclient

from analytics.google_products.authorization import Service
from analytics.google_products.google_analytics import GAUser


def ga_auth(client: str) -> googleapiclient.discovery.Resource:
    """authorize into the google analytics API"""
    service = Service("analytics", "v3", client).authenticate()
    ga_user = GAUser(service)
    return ga_user


def accounts_collection(user, account_ids):
    """return (account id, name) for selected accounts"""
    summaries = user.summaries()["items"]
    selected_accounts = [d for d in summaries if d["id"] in account_ids]
    ids = [d["id"] for d in selected_accounts]
    names = [d["name"] for d in selected_accounts]
    return list(zip(ids, names))


def filters_collection(user, account_ids):
    """return (account id, filter name) for selected accounts"""
    filters = [user.filters(i)["items"] for i in account_ids]
    ids = [i["accountId"] for f in filters for i in f]
    names = [i["name"] for f in filters for i in f]
    return list(zip(ids, names))


def properties_collection(user, account_ids):
    """return (property id, property name) for selected accounts"""
    properties = [user.properties(i)["items"] for i in account_ids]
    ids = [i["id"] for p in properties for i in p]
    names = [i["name"] for p in properties for i in p]
    return list(zip(ids, names))


def profiles_collection(user, account_ids):
    """return (property name, profile name) for selected accounts"""
    summaries = user.summaries()
    items = summaries["items"]
    selected_accounts = [d for d in items if d["id"] in account_ids]

    properties = [
        j["name"]
        for i in selected_accounts
        for j in i["webProperties"]
        for k in j["profiles"]
    ]

    names = [
        k["name"]
        for i in selected_accounts
        for j in i["webProperties"]
        for k in j["profiles"]
    ]

    return list(zip(properties, names))


def permissions_collection(user, account_ids):
    """return (email, permissions) for selected accounts"""
    perms = [user.users(i) for i in account_ids]
    users = [i["userRef"]["email"] for p in perms for i in p["items"]]
    access = [i["permissions"]["effective"] for p in perms for i in p["items"]]
    return list(zip(users, access))


def adwords_collection(user, account_ids):
    """return (property name, adwords ids / or names (??)) for selected accounts"""
    ids = [j["name"] for i in account_ids for j in user.properties(i)["items"]]

    # (we're getting the item list but we can add another nesting too)
    # (this is not finished yet)

    adwords = [
        user.adwords_links(j["accountId"], j["id"])["items"]
        for i in account_ids
        for j in user.properties(i)["items"]
    ]

    return list(zip(ids, adwords))


def custdims_collection(user, account_ids):
    """return (property name, custom dimensions) for selected accounts"""
    ids = [
        j["name"]
        for i in account_ids
        for j in user.properties(i)["items"]
        for k in user.custom_dimensions(j["accountId"], j["id"])["items"]
    ]

    names = [
        k["name"]
        for i in account_ids
        for j in user.properties(i)["items"]
        for k in user.custom_dimensions(j["accountId"], j["id"])["items"]
    ]

    return list(zip(ids, names))


def custmets_collection(user, account_ids):
    """return (property name, custom metrics) for selected accounts"""
    ids = [
        j["name"]
        for i in account_ids
        for j in user.properties(i)["items"]
        for k in user.custom_metrics(j["accountId"], j["id"])["items"]
    ]

    names = [
        k["name"]
        for i in account_ids
        for j in user.properties(i)["items"]
        for k in user.custom_metrics(j["accountId"], j["id"])["items"]
    ]

    return list(zip(ids, names))


def goals_collection(user, account_ids):
    """return (property name, goals) for selected account"""
    properties = [
        j["name"]
        for i in account_ids
        for j in user.properties(i)["items"]
        for k in user.views(j["accountId"], j["id"])["items"]
        for g in user.goals(k["accountId"], k["webPropertyId"], k["id"])[
            "items"
        ]
    ]

    names = [
        g["name"]
        for i in account_ids
        for j in user.properties(i)["items"]
        for k in user.views(j["accountId"], j["id"])["items"]
        for g in user.goals(k["accountId"], k["webPropertyId"], k["id"])[
            "items"
        ]
    ]

    return list(zip(properties, names))


if __name__ == "__main__":
    nvv_accounts = [
        "19884770",
        "154504229",
        "43705232",
        "29376776",
        "151911907",
        "51135343",
    ]

    gcp_client = "gcp-client.json"
    ga_user = ga_auth(gcp_client)

    pprint(accounts_collection(ga_user, nvv_accounts))
    pprint(filters_collection(ga_user, nvv_accounts))
    pprint(properties_collection(ga_user, nvv_accounts))
    pprint(profiles_collection(ga_user, nvv_accounts))
    pprint(permissions_collection(ga_user, nvv_accounts))
    pprint(adwords_collection(ga_user, nvv_accounts))
    pprint(custdims_collection(ga_user, nvv_accounts))
    pprint(custmets_collection(ga_user, nvv_accounts))
    pprint(goals_collection(ga_user, nvv_accounts))
