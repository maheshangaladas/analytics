"""
google tag manager audit (overview of accounts)
"""

from dataclasses import dataclass, field
from itertools import chain
from pprint import pprint

from googleapiclient.discovery import Resource

from analytics.google_products.authorization import Service
from analytics.google_products.google_tag_manager import GTMUser


@dataclass
class Audit(object):
    """given a user and list of accounts, run a bunch of checks"""

    account_ids: list = field(default_factory=list)
    client: str = field(default_factory=str)
    gtm_user: Resource = None
    account_paths: list = field(default_factory=list)
    container_paths: list = field(default_factory=list)
    workspace_paths: list = field(default_factory=list)

    def authenticate(self):
        service = Service("tagmanager", "v2", self.client).authenticate()
        self.gtm_user = GTMUser(service)
        return self

    def path_representation(self):
        self._account_representation()
        self._container_representation()
        self._workspace_representation()
        return self

    def _account_representation(self):
        accounts = self.gtm_user.accounts()["account"]
        accounts_subset = [
            d for d in accounts if d["accountId"] in self.account_ids
        ]
        self.account_paths = [d["path"] for d in accounts_subset]
        return accounts_subset

    def _container_representation(self):
        containers = [
            self.gtm_user.containers(p)["container"]
            for p in self.account_paths
        ]
        containers = list(chain.from_iterable(containers))
        self.container_paths = [d["path"] for d in containers]
        return containers

    def _workspace_representation(self):
        workspaces = [
            self.gtm_user.workspaces(p)["workspace"]
            for p in self.container_paths
        ]
        workspaces = list(chain.from_iterable(workspaces))
        self.workspace_paths = [d["path"] for d in workspaces]
        return workspaces

    def permission_representation(self):
        permissions = [
            self.gtm_user.permissions(p) for p in self.account_paths
        ]
        return permissions

    def tag_representation(self):
        tags = [self.gtm_user.tags(p)["tag"] for p in self.workspace_paths]
        return tags

    def trigger_representation(self):
        triggers = [self.gtm_user.triggers(p) for p in self.workspace_paths]
        return triggers

    def variable_representation(self):
        variables = [
            self.gtm_user.variables(p)["variable"]
            for p in self.workspace_paths
        ]
        return variables


if __name__ == "__main__":
    # there's a limit on requests per 100 seconds, who know what this limit is
    # google sure won't care to tell you

    nvv = ["87114"]
    gcp_client = "gcp-client.json"

    audit = Audit(account_ids=nvv, client=gcp_client).authenticate()
    print(audit)

    audit.path_representation()
    pprint(audit.permission_representation())
    pprint(audit.tag_representation())
    pprint(audit.trigger_representation())
    pprint(audit.variable_representation())

    print(audit)
