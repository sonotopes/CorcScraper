<h1> Scrape Estate</h1>

Web scraper that extracts real estate data/listings from the Corcoran website. 

## Prerequisites 

Python must be installed. All libraries from requirements.txt must also be installed. 

```
pip3 install -r requirements.txt
```

## Explication and Process

Listings are scraped from [Corcoran](https://www.corcoran.com/search/for-rent/location/new-york-ny-c900008/regionId/1?sortBy=listedDate%2Bdesc). To limit the scope of the project, the range of potential listings is limited to the NYC tri-state area. As such, the sample data usually includes up to 10,000 listings. On averge (since listings are taken down intermittently) Corcoran will host about 5,000 or so listings. This number varies by season. 

The scraper uses Playwright to handle javascript events (such as clicking onto the next page). As such, to avoid cloudflare detection or other software, the program randomizes the intervals with which it will initiate a click. Once the html has been extracted, the raw data will be excavated using Selectolax. 

The specific CSS selectors are defined in the config file. Once they have been located, the inner text content is parsed and processed into a CSV file. The data from the CSV file is standardized, and by the end of the program, a visual model is created (averge cost by neighborhood). 

## Important info 
To run the scraper, simply put in the command: 

```python3 MAIN_SCRAPER.py```

To change the number of listings processed, change 'Pages' in "tools.py".

'Pages' controls the number of webpages Playwright looks through. To look at fewer or more listings, simply change the value of 'Pages' to a number that is < 97 and atleast > 2. 

```
configurations = {
    "URL": 'https://www.corcoran.com/search/for-rent/location/new-york-ny-c900008/regionId/1?sortBy=listedDate%2Bdesc',
    "Pages": 10,
```
## Common Issues 



## Disclaimer

(*This application was made for purely educational purposes*)
