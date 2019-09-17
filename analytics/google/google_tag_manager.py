"""
google.google_tag_manager
.........................

functions for google tag manager API.

ref. https://developers.google.com/tag-manager/api/v2/devguide
"""


def gtm_list_accounts(service):
    """List Google Tag Manager accounts associated with a user.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :return: dictionary of accounts
    :rtype: dict
    """
    return service.accounts().list().execute()


def gtm_list_permissions(service, account_path):
    """List Google Tag Manager user permissions associated with a user.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :param account_path: path to Google Tag Manager account to inspect
    :type account_path: str
    :return: dictionary of user permissions
    :rtype: dict
    """
    return service.accounts().user_permissions().list(parent=account_path).execute()


def gtm_list_containers(service, account_path):
    """List Google Tag Manager containers associated with an account.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :param account_path: path to the Google Tag Manager account
    :type account_path: str
    :return: dictionary of containers
    :rtype: dict
    """
    return service.accounts().containers().list(parent=account_path).execute()


def gtm_list_workspaces(service, container_path):
    """List Google Tag Manager workspaces associated with a container.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :param container_path: path to the Google Tag Manager container
    :type container_path: str
    :return: dictionary of workspaces
    :rtype: dict
    """
    return (
        service.accounts()
        .containers()
        .workspaces()
        .list(parent=container_path)
        .execute()
    )


def gtm_list_environments(service, container_path):
    """List Google Tag Manager environments associated with a container.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :param container_path: path to the Google Tag Manager container
    :type container_path: str
    :return: dictionary of environments
    :rtype: dict
    """
    return (
        service.accounts()
        .containers()
        .environments()
        .list(parent=container_path)
        .execute()
    )


def gtm_list_variables(service, environment_path):
    """List Google Tag Manager variables associated with an environment.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :param environment_path: path to the Google Tag Manager environment
    :type environment_path: str
    :return: dictionary of variables
    :rtype: dict
    """
    return (
        service.accounts()
        .containers()
        .workspaces()
        .variables()
        .list(parent=environment_path)
        .execute()
    )


def gtm_list_tags(service, workspace_path):
    """List Google Tag Manager tags associated with a workspace.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :param workspace_path: path to the Google Tag Manager workspace
    :type workspace_path: str
    :return: dictionary of tags
    :rtype: dict
    """
    return (
        service.accounts()
        .containers()
        .workspaces()
        .tags()
        .list(parent=workspace_path)
        .execute()
    )


def gtm_list_triggers(service, workspace_path):
    """List Google Tag Manager triggers associated with a workspace.
    
    :param service: service object
    :type service: googleapiclient.discovery.Resource
    :param workspace_path: path to the Google Tag Manager workspace
    :type workspace_path: str
    :return: dictionary of triggers
    :rtype: dict
    """
    return (
        service.accounts()
        .containers()
        .workspaces()
        .triggers()
        .list(parent=workspace_path)
        .execute()
    )
