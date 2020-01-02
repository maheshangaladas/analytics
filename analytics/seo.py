"""
analytics.seo
.............

seo tools for analytics
"""

from collections import OrderedDict
from dataclasses import dataclass

from requests_html import HTMLSession


@dataclass
class URL:
    name: str

    def inspect(self) -> OrderedDict:
        """extract seo information from a URL"""
        session = HTMLSession()
        if self.name:
            response = session.get(self.name)
            response.html.render()
            status_code = response.status_code
            history = response.history
            encoding = response.encoding
            title = response.html.find("title", first=True).text
            links = response.html.absolute_links
            html = response.html
            raw_html = response.html.raw_html
            self.attributes = OrderedDict(
                [
                    ("response", response),
                    ("status_code", status_code),
                    ("history", history),
                    ("encoding", encoding),
                    ("title", title),
                    ("links", links),
                    ("html", html),
                    ("raw_html", raw_html),
                ]
            )
        else:
            raise ValueError(
                "please instantiate the URL class with a url name, e.g. URL('https://domainname.com')"
            )
        return self.attributes
