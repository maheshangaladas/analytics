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
    name: str = None
    attributes: OrderedDict() = None

    def inspect(self):
        """extract seo information from a URL"""
        session = HTMLSession()
        if self.name:
            response = session.get(self.name)
            status_code = response.status_code
            history = response.history
            encoding = response.encoding
            title = response.html.find("title", first=True).text
            # absolute_links(response.html.absolute_links)
            self.attributes = OrderedDict(
                [
                    ("response", response),
                    ("status_code", status_code),
                    ("history", history),
                    ("encoding", encoding),
                    ("title", title),
                ]
            )
        else:
            raise ValueError(
                "please instantiate the URL class with a url name, e.g. URL('https://domainname.com')"
            )
        return self.attributes


if __name__ == "__main__":
    # work in progress

    # url = URL("https://www.python.org/")
    # url = URL("https://www.avanza.se/start")
    url = URL("https://www.hemnet.se/")
    url.inspect()
    print(url.name)
    print(url.attributes)
