# Comparero Scraper
This is a scrapy project to scrape cars, bike, smartphones and laptop data from different sites.

## Setup
### Prerequisite
* python
* pip

```bash
# install package
pip install -r requirements.txt
# command to scrape and store data
scrapy crawl <crawler_name> -O <file-name>
# see scrapy commands to know about what files types are supported for file storage
```

## available crawlers
* itti: Scrape laptop specifications from https://itti.com.np/