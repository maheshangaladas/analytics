"""
analytics.google_tag_manager
............................

query the google tag manager API.

ref. https://developers.google.com/tag-manager/api/v2/devguide
"""

from dataclasses import dataclass
from typing import Dict

from googleapiclient.discovery import Resource


@dataclass
class GTMUser(object):
    service: object

    def accounts(self: Resource) -> Dict:
        """retrieve accounts for a user"""
        accounts = self.service.accounts().list().execute()
        return accounts

    def permissions(self: Resource, account_path: str) -> Dict:
        """retrieve user permissions for an account"""
        permissions = (
            self.service.accounts()
            .user_permissions()
            .list(parent=account_path)
            .execute()
        )
        return permissions

    def containers(self: Resource, account_path: str) -> Dict:
        """retrieve containers for an account"""
        containers = (
            self.service.accounts()
            .containers()
            .list(parent=account_path)
            .execute()
        )
        return containers

    def workspaces(self: Resource, container_path: str) -> Dict:
        """retrieve workspaces for a container"""
        workspaces = (
            self.service.accounts()
            .containers()
            .workspaces()
            .list(parent=container_path)
            .execute()
        )
        return workspaces

    def environments(self: Resource, container_path: str) -> Dict:
        """retrieve environments for a container"""
        environments = (
            self.service.accounts()
            .containers()
            .environments()
            .list(parent=container_path)
            .execute()
        )
        return environments

    def tags(self: Resource, workspace_path: str) -> Dict:
        """retrieve tags for a workspace"""
        tags = (
            self.service.accounts()
            .containers()
            .workspaces()
            .tags()
            .list(parent=workspace_path)
            .execute()
        )
        return tags

    def variables(self: Resource, workspace_path: str) -> Dict:
        """retrieve variables for a workspace"""
        variables = (
            self.service.accounts()
            .containers()
            .workspaces()
            .variables()
            .list(parent=workspace_path)
            .execute()
        )
        return variables

    def triggers(self: Resource, workspace_path: str) -> Dict:
        """retrieve triggers for a workspace"""
        triggers = (
            self.service.accounts()
            .containers()
            .workspaces()
            .triggers()
            .list(parent=workspace_path)
            .execute()
        )
        return triggers
