## Connecting to ListHub's API with Python

ListHub provides a [RESO](https://www.reso.org/reso-web-api/) Web API compliant service. [The API](https://developer.listhub.com/api/#making-requests) uses OAuth 2.0 for [authentication](https://developer.listhub.com/api/#authentication). _api.py_ implements a thin wrapper that demonstrates how to authenticate with a RESO compatible web service.


### Usage

The initialized client will automatically fetch and manage access tokens transparently in the background.

```python
from api import ListHubClient

# create expects LISTHUB_CLIENT_ID and
# LISTHUB_CLIENT_SECRET defined as environment
# variables.

client = ListHubClient.create()

# The API will return a JSON response with an array of
# listing JSON objects. See adapters.py to simplify
# working with the ListHub's json response objects.
listings = client.get_listings()
```

see _api.py_ for more details.

### N.B.:

1. Rate-limiting should be handled by the consuming code.
1. The listing query is hard-coded to properties valued over 1 million.
1. Filtering is left as an exercise for the user
