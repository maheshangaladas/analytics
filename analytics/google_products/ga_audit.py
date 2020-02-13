from pprint import pprint

import googleapiclient

from analytics.google_products.authorization import Service
from analytics.google_products.google_analytics import GAUser

# from typing import Dict, List


# no automatic checks instead:
# - create summaries
# - write summaries to file
# - inspect and evaluate files manually


def ga_auth(client: str) -> googleapiclient.discovery.Resource:
    """authorize into google analytics API"""
    service = Service("analytics", "v3", client).authenticate()
    ga_user = GAUser(service)
    return ga_user


def account_collection(user, account_ids):
    summaries = user.summaries()["items"]
    selected_accounts = [d for d in summaries if d["id"] in account_ids]
    ids = [d["id"] for d in selected_accounts]
    names = [d["name"] for d in selected_accounts]
    return list(zip(ids, names))


def filter_collection(user, account_ids):
    filters = [user.filters(i)["items"] for i in account_ids]
    ids = [i["accountId"] for f in filters for i in f]
    names = [i["name"] for f in filters for i in f]
    return list(zip(ids, names))


def property_collection(user, account_ids):
    properties = [user.properties(i)["items"] for i in account_ids]
    ids = [i["id"] for p in properties for i in p]
    names = [i["name"] for p in properties for i in p]
    return list(zip(ids, names))


def profile_collection(user, account_ids):
    summaries = user.summaries()
    items = summaries["items"]
    selected_accounts = [d for d in items if d["id"] in account_ids]

    ids = [
        j["id"]
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

    return list(zip(ids, names))


def permission_collection(user, account_ids):
    perms = [user.users(i) for i in account_ids]
    users = [i["userRef"]["email"] for p in perms for i in p["items"]]
    access = [i["permissions"]["effective"] for p in perms for i in p["items"]]
    return list(zip(users, access))


def adwords_collection(user, account_ids):
    ids = [j["id"] for i in account_ids for j in user.properties(i)["items"]]

    # (we're getting the item list but we can add another nesting too)

    adwords = [
        user.adwords_links(j["accountId"], j["id"])["items"]
        for i in account_ids
        for j in user.properties(i)["items"]
    ]

    return list(zip(ids, adwords))


def custdim_collection(user, account_ids):
    ids = [
        j["id"]
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


def custmet_collection(user, account_ids):
    ids = [
        j["id"]
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


def goals_collection(user, accout_ids):
    pass


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

    # pprint(account_collection(ga_user, nvv_accounts))
    # pprint(filter_collection(ga_user, nvv_accounts))
    # pprint(property_collection(ga_user, nvv_accounts))
    # pprint(profile_collection(ga_user, nvv_accounts))
    # pprint(permission_collection(ga_user, nvv_accounts))
    # pprint(adwords_collection(ga_user, nvv_accounts))
    # pprint(custdim_collection(ga_user, nvv_accounts))
    pprint(custmet_collection(ga_user, nvv_accounts))
