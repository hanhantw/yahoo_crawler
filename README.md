# Yahoo_crawler

This is a project for clawing best selling products on yahoo

## Prerequisites

* python2.7
* scrapy1.5.1

## Selecting Rules
```
Rule(LinkExtractor(allow=('/?sub=\d+')), follow=True),
Rule(LinkExtractor(allow=('/?catitemid=\d+')), follow=True),
Rule(LinkExtractor(allow=('/?catitemid=\d+&sort=-tsales&pg=\d+')), callback='parse_item',follow=True),
```
## Output
* JSON file
