## Table of Contents <!-- omit in toc -->
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Google Tag Manager](#google-tag-manager)

**analytics** allows you to communicated with standard web analytics tools. It does not expose all of the functionalities for these services but focuses on the most general ones.

## Features

- Interface with Google Tag Manager API.

## Installation

```bash
python3 -m pip install git+git://github.com/xslates/analytics.git
```

## Usage

### Authentication

Authentication on Google APIs uses service account credentials or a client ID and client secret credentials (which is the default method). In both cases, you need a Google Cloud Platform account. You will need to download the JSON files from your Google Cloud Platform account. If you use the service account authorization method, remember to give access permissions to your service account email from within your tools (Google Analytics, Google Tag Manager, and other Google products)

When you run the client authorization flow the first time, you'll be prompted to authorize via the web browser flow. It will store a token for the API you're trying to access in the directory you're in (or the root directory). If you move its location, `get_service` will not be able to find it, so keep it where it is—the same goes for your `gcp_client` file. If you want to authorize as a different user, delete the .dat file and run `get_service` again.

```python
gtm_service = get_service("tagmanager", "v2", gcp_client)

# or

gtm_service = gtm_service("tagmanager", "v2", gcp_client, method="service_account")
```

### Google Tag Manager

For ease of use, all of the functions in the Google Tag Manager module return Pandas data frames.

```python
# list accounts
accounts = gtm_list_accounts(gtm_service)
```

```python
# list permissions for a given account
account = accounts.iloc[0, 0]
permissions = gtm_list_permissions(gtm_service, account)
```

```python
# list containers for a given account
containers = gtm_list_containers(gtm_service, account)
```

```python
# list workspaces for a given container
container = containers.iloc[0, 0]
workspaces = gtm_list_workspaces(gtm_service, container)
```

```python
# list environments for a given container
environments = gtm_list_environments(gtm_service, container)
```

```python
# list variables for a given workspace
workspace = workspaces.iloc[0, 0]
variables = gtm_list_variables(gtm_service, workspace)
```

```python
# list tags for a given workspace
tags = gtm_list_tags(gtm_service, workspace)
```

```python
# list triggers for a given workspace
triggers = gtm_list_triggers(gtm_service, workspace
```