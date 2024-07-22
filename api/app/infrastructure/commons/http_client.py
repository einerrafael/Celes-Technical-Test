import requests


class HttpClient:

    @staticmethod
    def post(url, **kwargs):
        return requests.request('POST', url, **kwargs)
