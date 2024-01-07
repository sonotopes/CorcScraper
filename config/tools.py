import json

configurations = {
    "URL": 'https://www.corcoran.com/search/for-rent/location/new-york-ny-c900008/regionId/1?sortBy=listedDate%2Bdesc',
    "Pages": 10,
    # "Text" attribute indicates whether HTML text can be accessed directly. If false, the item is a node, and the text
    # is nested within another element. If true, text can be immediately accessed.

    # "Match" attribute indicates whether selectolax will locate the first instance of the selector, or, every
    # instance.

    "body_node":
        {
            "name": "listing_div",
            "selector": 'div[class*="ListingCard__ListingCardWrapper"]',
            "secondary_selector": None,
            "text": False,
            "required": True,

        },
    "item": [
        {
            "name": "address",
            "selector": 'h2[class*="ListingCard__Street"]',
            "secondary_selector": None,
            "text": True,
            "required": True,
        },

        {
            "name": "location",
            "selector": 'div[class*="ListingCard__Location"]',
            "secondary_selector": None,
            "text": True,
            "required": True,
        },

        {
            "name": "type",
            "selector": 'li[class*="ListingCardDetails__PropertyInfoSummary"]',
            "secondary_selector": None,
            "text": True,
            "required": True,
        },

        {
            "name": "price",
            "selector": 'div[class*="ListingCard__PriceWrapper"] > div',
            "secondary_selector": None,
            "text": True,
            "required": True,
        },

        {
            "name": "listing_image",
            "selector": 'div[class*="ListingCard__ImageContainer"] > img',
            "secondary_selector": None,
            "text": False,
            "required": True,
        },

        {
            "name": "beds",
            "selector": 'li[data-testid*="beds"]',
            "secondary_selector": None,
            "text": True,
            "required": False,
        },

        {
            "name": "baths",
            "selector": 'li[data-testid*="baths"]',
            "secondary_selector": None,
            "text": True,
            "required": False,
        },
        {
            "name": "half_baths",
            "selector": 'li[data-e2e-id*="listing-card__property-info-half-baths"]',
            "secondary_selector": None,
            "text": True,
            "required": False,
        },
        {
            "name": "square_feet",
            "selector": 'li[data-e2e-id*="listing-card__property-info-square-feet"]',
            "secondary_selector": None,
            "text": True,
            "required": False,
        },
        {
            "name": "brokerage",
            "selector": 'div[class*="ListingCard__ListingAttributionText"] > div > span',
            "secondary_selector": 'div[class*="ListingCard__ListingAttribution"] > '
                                  'div[class*="ListingCard__ListingAttributionText"]',
            "text": True,
            "required": False,
        },
        {
            "name": "attribution",
            "selector": 'div[class*="ListingCard__ListingAttribution"] > div['
                        'class*="ListingCard__ListingAttributionImageWrapper"] > '
                        'img',
            "secondary_selector": None,
            "text": False,
            "required": False,
        }
    ],
}


def get_config(load_from_file=False):
    """Returns config settings. If indicated, will load from a separate json file."""
    if load_from_file:
        with open("config.json", "r") as j:
            return json.load(j)
    return configurations


def generate_config():
    """Generates config file."""
    with open("config.json", "w") as j:
        json.dump(configurations, j, indent=6)


if __name__ == "__main__":
    generate_config()
