import requests, logging, time, os, ujson

from requests.adapters import HTTPAdapter

from requests.packages.urllib3.util.retry import Retry


class ListHubQuery:
    def __init__(self, next_url=None):
        self.next_url = next_url
        self.base_url = "https://api.listhub.com/odata/Property?$filter=PropertyType eq 'Land' and ListPrice ge 1000000"

    @property
    def as_url(self):
        if self.next_url:
            return self.next_url
        else:
            return self.base_url


class ListHubClient:
    def __init__(self, access_token):
        self.authorization_header = {"Authorization": f"Bearer {access_token}"}

    @classmethod
    def create(cls):
        payload = {
            "client_id": os.getenv("LISTHUB_CLIENT_ID"),
            "client_secret": os.getenv("LISTHUB_CLIENT_SECRET"),
            "grant_type": "client_credentials",
        }

        response = requests.post("https://api.listhub.com/oauth2/token", data=payload)

        return cls(response.json()["access_token"])

    def get(self, url):
        headers = {**self.authorization_header, **{"User-Agent": "data-fetch"}}

        retry_strategy = Retry(total=3, backoff_factor=2)

        adapter = HTTPAdapter(max_retries=retry_strategy)

        http = requests.Session()

        http.mount("https://", adapter)

        response = http.get(url, headers=headers, timeout=(3.00, 57))

        return response

    def get_listings(self, skip_url=None):
        query = ListHubQuery(skip_url)

        return self.get(query.as_url)
