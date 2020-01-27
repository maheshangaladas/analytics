"""
analytics.utm_tags
..................

generate UTM tags

ref. https://ga-dev-tools.appspot.com/campaign-url-builder/
"""

import re
from typing import Optional


def utm_tag(
    url: str,
    source: str,
    medium: str,
    name: str,
    term: Optional[str] = None,
    content: Optional[str] = None,
) -> str:

    term = re.sub(r" ", "%2B", term) if term else None
    content = re.sub(r" ", "%2B", content) if content else None

    website_url = url + "?" if url.endswith("/") else url + "/?"
    campaign_source = "utm_source=" + source
    campaign_medium = "utm_medium=" + medium
    campaign_name = "utm_campaign=" + name
    campaign_term = "utm_term=" + term if term else ""
    campaign_content = "utm_content=" + content if content else ""

    strings = [
        website_url,
        campaign_source,
        campaign_medium,
        campaign_name,
        campaign_term,
        campaign_content,
    ]

    tag = "&".join(s for s in strings if s)
    tag = re.sub(r"&", "", tag, 1)

    return tag
