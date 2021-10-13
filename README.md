## Connecting to ListHub API with Python

The [Syndication API](https://developer.listhub.com/api/#making-requests) uses OAuth 2.0 for authentication. `api.py` implements a thin wrapper around ListHub's Syndication API-- enough to get started.


### Usage

```python
from api import ListHubClient

# create returns a listhub client instantiated
# with a new authentication token
# create expects LISTHUB_CLIENT_ID and
# LISTHUB_CLIENT_SECRET defined as environment
# variables.

client = ListHubClient.create()

listings = client.get_listings()
```

### N.B.:

1. Rate-limiting should be handled by the consuming code.
1. The listing query is hard-coded to properties valued over 1 million.
1. Filtering is left as an exercise for the user
