## Table of Contents <!-- omit in TOC -->
- [Installation](#installation)
- [Imports](#imports)
- [Authorization](#authorization)
- [Google Tag Manager](#google-tag-manager)
- [Google Analytics (Management)](#google-analytics-management)
- [Google Analytics Reporting](#google-analytics-reporting)
- [JSON vs Pandas for Google Tag Manager and Google Analytics Management](#json-vs-pandas-for-google-tag-manager-and-google-analytics-management)

## Installation

```bash
python3 -m pip install git+git://github.com/xslates/analytics.git
```

## Imports

```python
from analytics.google_tag_manager import *
from analytics.google_analytics import *
from analytics.authorization import *
```

## Authorization

You can authorize using service accounts or client tokens. Given that you've downloaded either, you can authenticate like this:

```python
gcp_service = "/Users/username/gcp-service.json"
gcp_client = "/Users/username/gcp-client.json"

# Google Tag Manager
service = Service("tagmanager", "v2", gcp_client).authenticate() # or gcp_service
user = GTMUser(service)

# Google Analytics
service = Service("analytics", "v3", gcp_client).authenticate() # or gcp_service
user = GAUser(service
```

If you use service accounts, remember to give permissions to your service account email on the platforms you want to access.

The first time you authenticate, you'll be taken through a browser flow. After that, a token will be stored in your working directory. Keep it there! **analytics** uses that token in subsequent authentication attempts. 

- If you want to authenticate as a different user, just delete the token and re-run the authentication.
- If you move the token file to another location, **analytics** will not be able to find it.

## Google Tag Manager

`analytics.google_tag_manager` offers functionality to retrieve information from your Google Tag Manager accounts.

```python
# example values from a google tag manager account

accountpath = "accounts/4703034098" 
containerpath = "accounts/4703034098/containers/13195950"
workspacepath = "accounts/4703034098/containers/13195265/workspaces/5"

accounts = user.accounts()
print(accounts

permissions = user.permissions(accountpath)
print(permissions)

containers = user.containers(accountpath)
print(containers)

environments = user.environments(containerpath)
print(environments)

workspaces = user.workspaces(containerpath)
print(workspaces)

tags = user.tags(workspacepath)
print(tags)

variables = user.variables(workspacepath)
print(variables)

triggers = user.triggers(workspacepath)
print(triggers)
```

## Google Analytics (Management)

`analytics.google_analytics` offers functionality to retrieve information from your Google Analytics account.

```python
# example values from a google analytics account

accountid = "3100168"
propertyid = "UA-3100168-49"
viewid = "169728486"

summaries = user.summaries()
print(summaries)

accounts = user.accounts()
print(accounts)

users = user.users(accountid)
print(users)

properties = user.properties(accountid)
print(properties)

adwords = user.adwords_links(accountid, propertyid)
print(adwords)

dimensions = user.custom_dimensions(accountid, propertyid)
print(dimensions)

metrics = user.custom_metrics(accountid, propertyid)
print(metrics)

filters = user.filters(accountid)
print(filters)

views = user.views(accountid, propertyid)
print(views)

goals = user.goals(accountid, propertyid, viewid)
print(goals)

remarketing = user.remarketing(accountid, propertyid)
print(remarketing)

segments = user.segments()
print(segments)
```

## Google Analytics Reporting

( ... WIP)

## JSON vs Pandas for Google Tag Manager and Google Analytics Management

You might wonder why **analytics** doesn't provide `pandas` data frames instead of JSON response dictionaries. It is a deliberate decision, and the explanation is pretty straight-forward. Google's JSON API responses are some of the worst, and I had a detestable time trying to wrangle them into data frames. 

It turned out impractical to find ways to parse the responses into intelligible, nevermind useful, datasets. The `parameter` key for variables, tags, and triggers in Google Tag Manager are the main offenders. 

For these reasons, I decided to leave the JSON responses intact in the original API calls. Rather than provide a half-assed solution, I chose not to provide any.  `json_normalize` [(documentation link)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.json.json_normalize.html) is your best bet at making datasets out of these responses. However, it breaks when parsing Google's parameter keys. If you have better ideas for parsing these responses into data frames, please make a pull request.