import requests


def get(path: str, data: dict[str,]) -> requests.Request:
    if path[0] == '/':
        path = path[1:]
    url = 'https://maplestory.nexon.com/' + path
    header = {
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
    }
    return requests.post(url=url, data=data, headers=header)
