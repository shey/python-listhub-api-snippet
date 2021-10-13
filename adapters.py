import arrow, ujson


class ResponseEnvelope:
    def __init__(self, api_response):
        self.json_obj = ujson.loads(api_response.content)

    @property
    def listings(self):
        return [Listing(l) for l in self.json_obj["value"]]

    @property
    def next_page_url(self):
        return self.json_obj.get("@odata.nextLink", None)


class Listing:
    def __init__(self, primitive_listing_obj):
        self.listing_obj = primitive_listing_obj

    @property
    def listing_key(self):
        return self.listing_obj["ListingKey"]

    @property
    def last_update(self):
        return arrow.get(self.listing_obj["ModificationTimestamp"])
