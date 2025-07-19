Crypto Tracker

A simple Python project to fetch cryptocurrency prices, store them in PostgreSQL, and visualize them using matplotlib.

Features

Fetch real-time crypto prices using public APIs

Store data in a PostgreSQL database

Generate price trend plots with matplotlib

Automated data fetch using shell script and cron jobs

Setup Instructions

Clone the repo:

git clone https://github.com/Allan-Wamae/crypto-tracker.git
cd crypto-tracker

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Set up PostgreSQL:

Make sure PostgreSQL is installed and running.

Create a database (e.g., crypto_db):

CREATE DATABASE crypto_db;

Create the crypto_prices table:

CREATE TABLE crypto_prices (
id SERIAL PRIMARY KEY,
name TEXT NOT NULL,
symbol TEXT NOT NULL,
price_usd NUMERIC,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Create a .env file in the root directory with your credentials:

DB_NAME=crypto_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

Run the fetch script manually:

python fetch_crypto_data.py

Visualize the data:

python plot_crypto.py

Automate data fetching (optional):

Run the shell script manually:

./fetch_data.sh

Or schedule it with a cron job:

crontab -e

Add a line like:

0 \* \* \* \* /path/to/crypto-tracker/fetch_data.sh

Usage

Run fetch_crypto_data.py to fetch and store prices.

Run plot_crypto.py to visualize the data.

Use cron or shell script to automate hourly/daily fetching.

License

MIT License © Allan Wamai
