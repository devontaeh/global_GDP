# web-scraping-tutorial
## Overview
This project demonstrates a simple web scraping technique using Python to extract a list of countries and their Gross Domestic Product (GDP) in billions of USD from a Wikipedia page. The data is then transformed, saved to a CSV file, and loaded into an SQLite database.

## Purpose
This tutorial aims to provide a basic understanding of web scraping, data transformation, and data storage using popular Python libraries such as pandas, numpy, BeautifulSoup, and sqlite3.

## Requirements
- Python 3.x
- Libraries: **pandas**, **numpy**, **BeautifulSoup**, **requests**, **sqlite3**
- Internet connection for web scraping
## Installation
Before running the script, please ensure the required libraries are installed. You can install these using pip:

```bash
pip install pandas numpy beautifulsoup4 requests
```
## Usage
1. **Extract Data**: The script scraps the GDP data from a specified Wikipedia page.
2. **Transform Data**: The GDP values, initially in millions, are converted to billions for easier comprehension.
3. **Load Data**: The transformed data is then saved to a CSV file and loaded into an SQLite database.
4. **Query Data**: The script runs a SQL query to display countries with a GDP of over $100 billion.
## Running the Script
- Run the script in a Python environment.
- The script logs its progress, saving timestamps and messages to etl_project_log.txt.
- Adjust the url, table_attribs, db_name, table_name, and csv_path variables as needed.
## Notes
- This script is a basic tutorial and should be used for educational purposes.
- The reliability of the data depends on the source web page's current structure and content.
