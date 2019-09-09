import random

from mitmproxy import http
import typing

def proxy_address(flow: http.HTTPFlow) -> typing.Tuple[str, int]:
    # Poor man's loadbalancing: route every second domain through the alternative proxy.
    # if hash(flow.request.host) % 2 == 1:
    #     return ("192.168.1.2", 8888)
    # else:
    #     return ("192.168.1.5", 8888)
    proxy_list = [("192.168.1.2", 8888),("192.168.1.5", 8888)]
    proxy = random.choice(proxy_list)
    return proxy


def request(flow: http.HTTPFlow) -> None:
    # if flow.request.method == "CONNECT":
    #     # If the decision is done by domain, one could also modify the server address here.
    #     # We do it after CONNECT here to have the request data available as well.
    #     return
    address = proxy_address(flow)
    if flow.live:
        print(address)
        flow.live.change_upstream_proxy_server(address)