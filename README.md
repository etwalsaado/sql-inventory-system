
# SQL Inventory System

## Project Overview
A Python project that uses SQLite and SQL to retrieve product data and calculate basic manufacturing KPIs.

## Technologies
- Python
- SQLite
- SQL

## Features
- Count total products.
- Count successful and failed products using SQL.
- Calculate the success rate.
- Join product and machine tables to display product-machine relationships.

## Database
The project uses an SQLite database (`inventory.db`) with two main tables:
- `products`
- `machines`

## How to Run
1. Install Python 3.
2. Open a terminal in the project directory.
3. Run:

```bash
python app.py
```

## Skills Practiced
- Connecting Python to SQLite.
- SQL queries using `SELECT`, `COUNT`, `CASE WHEN`, and `JOIN`.
- Retrieving and processing query results in Python.
- Calculating basic KPIs.
