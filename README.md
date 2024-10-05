<h1> CorcScraper </h1>

Web scraper that extracts real estate data/listings from the Corcoran website. 

## Prerequisites 

Python must be installed. All libraries from requirements.txt must also be installed. 

```
pip3 install -r requirements.txt
```

## Data Visualization using PowerBI. 

[Dashboard](https://app.powerbi.com/groups/59250128-3298-4baa-ae98-173027907efd/reports/ade75a10-6ad3-4463-8b70-7d4d9294f436?ctid=ce6d05e1-3c5e-4d62-87a8-4c4a2713c113&pbi_source=linkShare&bookmarkGuid=357999d4-6df9-4e7b-bca2-c4c57ce1197f)


![Scraping-4-1](https://github.com/user-attachments/assets/3fc24a8c-140f-4ad7-b7f6-90642824de70)

Report from scraping approximately 4,000 listings in the NYC area. 

## Explication and Process

Listings are scraped from [Corcoran](https://www.corcoran.com/search/for-rent/location/new-york-ny-c900008/regionId/1?sortBy=listedDate%2Bdesc). To limit the scope of the project, the range of potential listings is limited to the NYC tri-state area. As such, the sample data usually includes up to 10,000 listings. On average (since listings are taken down intermittently) Corcoran will host about 5,000 or so listings. This number varies by season. 

The scraper uses Playwright to handle javascript events (such as navigating to the next page). As such, to avoid cloudflare detection or other software, the program randomizes the intervals with which it will initiate a click. Once the html has been extracted, the raw data will be excavated using Selectolax. 

The specific CSS selectors are defined in the config file. Once they have been located, the inner text content is parsed and processed into CSV format. The data from the CSV file is standardized, and by the end of the program, a visual model is created (of average cost by neighborhood). 

*Data should look like this:*
![data](https://i.postimg.cc/yd6YQw8c/Screenshot-79.png)

## Important info 

To begin, simply run the command: 

```python3 main.py```

(*Note: The program may take a few minutes to extract the data.*)

To change the number of listings processed, change 'Pages' in "tools.py".

'Pages' controls the number of webpages Playwright looks through. To look at fewer or more listings, simply change the value of 'Pages' to a number that is < 97 and atleast > 2. 

```
configurations = {
    "URL": 'https://www.corcoran.com/search/for-rent/location/new-york-ny-c900008/regionId/1?sortBy=listedDate%2Bdesc',
    "Pages": 10,
```
## Common Issues 

```asyncio.exceptions.InvalidStateError: invalid state```

This usually occurs because Playwright's request to the website times out. One reason for this is that the number listed on 'Pages' exceeds the number on the website's navigation bar. If this isn't the case, then it's usually is an issue with the site itself. To fix this issue, the solution is to input a smaller number for the 'Pages' attribute, or, try to run the program at a different time. 

## Disclaimer

(*This application was made for purely educational purposes*)
