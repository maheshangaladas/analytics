from collections import OrderedDict
from pprint import pprint
from typing import Dict, List

import googleapiclient

from analytics.google_products.authorization import Service
from analytics.google_products.google_analytics import GAUser

# no automatic checks instead:
# - create summaries
# - write summaries to file
# - inspect and evaluate files manually


def ga_auth(client: str) -> googleapiclient.discovery.Resource:
    """authorize into google analytics API"""
    service = Service("analytics", "v3", client).authenticate()
    ga_user = GAUser(service)
    return ga_user


def ga_accounts_audit(
    user: googleapiclient.discovery.Resource, account_ids: List[str]
) -> Dict:
    """retrieve overview for a list of google analytics accounts"""
    summaries = user.summaries()
    items = summaries["items"]
    accounts = [d for d in items if d["id"] in account_ids]
    account_names = [d["name"] for d in accounts]
    properties_names = [
        j["name"] for i in accounts for j in i["webProperties"]
    ]
    properties_ids = [j["id"] for i in accounts for j in i["webProperties"]]
    n_properties = len(properties_names)
    profile_names = [
        k["name"]
        for i in accounts
        for j in i["webProperties"]
        for k in j["profiles"]
    ]
    profile_ids = [
        k["id"]
        for i in accounts
        for j in i["webProperties"]
        for k in j["profiles"]
    ]
    n_profiles = len(profile_names)

    overview: Dict = OrderedDict(
        [
            ("account_names", account_names),
            ("properties_name", properties_names),
            ("properties_tally", n_properties),
            ("properties_ids", properties_ids),
            ("profile_names", profile_names),
            ("profiles_tally", n_profiles),
            ("profile_ids", profile_ids),
        ]
    )

    return overview


def ga_permissions_audit(
    user: googleapiclient.discovery.Resource, account_ids: List[str]
) -> Dict:
    """retrieve permissions overview for a list of google analytics accounts"""
    permissions = [user.users(i) for i in account_ids]
    effective_permissions = [
        j["permissions"]["effective"] for i in permissions for j in i["items"]
    ]
    user_reference = [
        j["userRef"]["email"] for i in permissions for j in i["items"]
    ]
    overview: Dict = OrderedDict(zip(user_reference, effective_permissions))
    return overview


def ga_properties_audit(user: googleapiclient.discovery.Resource):
    summaries = user.summaries()["items"]
    # we need to create a dictionary of account_id, property_id
    # we then can decompose it in the call to funcs like custom_metrics
    return summaries


def ga_profiles_audit(user: googleapiclient.discovery.Resource):
    summaries = user.summaries()["items"]
    # we need a dict of account_id, property_id, view_id
    # we then decompose it to make call to funcs like goals
    return summaries


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
    accounts = ga_accounts_audit(ga_user, nvv_accounts)
    permissions = ga_permissions_audit(ga_user, nvv_accounts)
    # pprint(accounts)
    # pprint(permissions)
    properties = ga_properties_audit(ga_user)
    pprint(properties)
