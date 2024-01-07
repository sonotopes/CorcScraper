<h1> Scrape Estate</h1>

Web scraper that extracts real estate data/listings from the Corcoran website. 

## Prerequisites 

Python must be installed. All libraries from requirements.txt must also be installed. 

```
pip3 install -r requirements.txt
```

## Explication 

Listings are scraped from [Corcoran](https://www.corcoran.com/search/for-rent/location/new-york-ny-c900008/regionId/1?sortBy=listedDate%2Bdesc). To limit the scope of the project, the range of potential listings is limited to the NYC tri-state area. As such, the sample data usually includes up to 10,000 listings. On averge (since listings are taken down intermittently) the Corcoran will host about 5,000 or so listings depending on the season. 

The scraper uses Playwright to handle javascript events (such as clicking onto the next page). To avoid cloudflare detection or other software then, the program randomizes 


## Disclaimer

(*This application was made for purely educational purposes*)
