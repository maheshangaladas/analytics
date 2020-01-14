"""
analytics.webmetrics
.................

lists of useful website metrics
"""

from typing import List

performance_metrics = [
    "page speed",
    "time to interactive",
    "page load time",
    "requests per second",
    "time to first byte",
    "speed index",
    "DNS lookup time",
    "uptime",
    "time to first paint",
    "time to first contentful paint",
    "onload time",
    "total page size",
    "fully loaded time",
    "DOM content loaded",
    "HTTP requests",
]


def metrics_list(kind: List[str]) -> List:
    """list web metrics"""
    metrics = kind
    return metrics
