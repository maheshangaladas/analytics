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

    website_url = url + "?" if url.endswith("/") else url + "/?"
    campaign_source = "utm_source=" + source
    campaign_medium = "utm_medium=" + medium
    campaign_name = "utm_campaign=" + name
    # the utm builder handles concatenation of terms differently (look into it)
    # terms can be compounded, have plus signs, empty spaces, etc. between them
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
