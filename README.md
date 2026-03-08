# Product Web Scraper (Python)

## Overview

This project is a beginner-friendly web scraping script built with Python.
It collects product information from an e-commerce website and saves the data into a CSV file.

The script extracts product details from the listing page and then visits each product page to collect additional information.

## Features

* Scrapes product name
* Scrapes product price
* Visits each product page
* Extracts product availability
* Extracts product description
* Saves all data into a CSV file

## Technologies Used

* Python
* Requests
* BeautifulSoup (bs4)
* CSV

## How It Works

1. Sends a request to the product listing page.
2. Parses the HTML using BeautifulSoup.
3. Finds all product cards on the page.
4. Extracts the product name and price.
5. Opens each product's detail page.
6. Extracts availability and description.
7. Saves the collected data into `products.csv`.

## Installation

Install required packages:

```
pip install requests beautifulsoup4
```

## How to Run

Run the script using:

```
python main.py
```

After running, a file called `products.csv` will be created containing the scraped data.

## Output Example

| Product Name    | Product Price | Availability | Description              |
| --------------- | ------------- | ------------ | ------------------------ |
| Example Product | $120          | In Stock     | Product description text |

## Project Structure

```
project-folder
│
├── main.py
├── products.csv
└── README.md
```

