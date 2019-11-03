"""
analytics.google_tag_manager
............................

query the google tag manager API

ref. https://developers.google.com/tag-manager/api/v2/devguide
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class GTMUser(object):
    service: object

    def accounts(self: object) -> Dict:
        accounts = self.service.accounts().list().execute()
        return accounts

    def permissions(self: object, account_path: str) -> Dict:
        permissions = (
            self.service.accounts()
            .user_permissions()
            .list(parent=account_path)
            .execute()
        )
        return permissions

    def containers(self: object, account_path: str) -> Dict:
        containers = (
            self.service.accounts()
            .containers()
            .list(parent=account_path)
            .execute()
        )
        return containers

    def workspaces(self: object, container_path: str) -> Dict:
        workspaces = (
            self.service.accounts()
            .containers()
            .workspaces()
            .list(parent=container_path)
            .execute()
        )
        return workspaces

    def environments(self: object, container_path: str) -> Dict:
        environments = (
            self.service.accounts()
            .containers()
            .environments()
            .list(parent=container_path)
            .execute()
        )
        return environments

    def tags(self: object, workspace_path: str) -> Dict:
        tags = (
            self.service.accounts()
            .containers()
            .workspaces()
            .tags()
            .list(parent=workspace_path)
            .execute()
        )
        return tags

    def variables(self: object, workspace_path: str) -> Dict:
        variables = (
            self.service.accounts()
            .containers()
            .workspaces()
            .variables()
            .list(parent=workspace_path)
            .execute()
        )
        return variables

    def triggers(self: object, workspace_path: str) -> Dict:
        triggers = (
            self.service.accounts()
            .containers()
            .workspaces()
            .triggers()
            .list(parent=workspace_path)
            .execute()
        )
        return triggers
