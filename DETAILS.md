## Table of Contents <!-- omit in toc -->
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Google Tag Manager](#google-tag-manager)
  - [Google Analytics (Management API)](#google-analytics-management-api)

**analytics** allows you to communicate with standard web analytics tools. It does not expose all of the functionalities for these services but focuses on the most general ones.

## Features

- Interface with Google Tag Manager API.

## Installation

```bash
python3 -m pip install git+git://github.com/xslates/analytics.git
```

## Usage

### Authentication

Authentication on Google APIs uses service account credentials or a client ID and client secret credentials (which is the default method). In both cases, you need a Google Cloud Platform account. You will need to download the JSON files from your Google Cloud Platform account. If you use the service account authorization method, remember to give access permissions to your service account email from within your tools (Google Analytics, Google Tag Manager, and other Google products)

When you run the client authorization flow the first time, you'll be prompted to authorize via the web browser flow. It will store a token for the API you're trying to access in the directory you're in (or the root directory). If you move its location, `get_service` will not be able to find it, so keep it where it is—the same goes for your `gcp_client` or `gcp_service` file which should reference the path where you've stored that file. If you want to authorize as a different user, delete the .dat file and run `get_service` again.

```python
from analytics.authorization import get_service
from analytics.google_tag_manager import *
```

### Google Tag Manager

For ease of use, all of the functions in the Google Tag Manager module return Pandas data frames.

```python
gtm_service = get_service("tagmanager", "v2", gcp_client)

# or

gtm_service = gtm_service("tagmanager", "v2", gcp_service, method="service_account")
```

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

### Google Analytics (Management API)

For ease of use, all of the functions in the Google Analytics module return Pandas data frames.

```python
ga_service = get_service("analytics", "v3", gcp_client)

# or

ga_service = gtm_service("analytics", "v3", gcp_service, method="service_account")
```
```python
# list account summaries
summaries = ga_list_account_summaries(ga_service)
```

```python
# list accounts a user has access to
accounts = ga_list_accounts(ga_service)
account = accounts.iloc[0, 0]
```

```python
# list properties in an account
properties = ga_list_webproperties(ga_service, account)
webprop = properties.iloc[0, 0]
```

```python
# list users in an account
users = ga_list_account_users(ga_service, account)
```

```python
# list adwords accounts linked to a property
adwords_links = ga_adwords_links(ga_service, account, webprop)
```

```python
# list custom dimensions in a web property
custom_dimensions = ga_list_custom_dimensions(ga_service, account, webprop)
```

```python
# list custom metrics in a web property
custom_metrics = ga_list_custom_metrics(ga_service, account, webprop)
```

```python
# list filters in an account
filters = ga_list_filters(ga_service, account)
```

```python
# list views in a web proerty
views = ga_list_views(ga_service, account, webprop)
view = views.iloc[0, 0]
```

```python
# list goals in a view
goals = ga_list_goals(ga_service, account, webprop, view)
```

```python
# list remarketing audiences in a web property
audiences = ga_list_remarketing_audiences(ga_service, account, webprop)
```

```python
# list segments associated with an account
segments = ga_list_segments(ga_service)
```