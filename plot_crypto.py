import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt


# Connecting to database
conn = psycopg2.connect(
    dbname="crypto_db",
    user="allan",
    password="78student73",
    host="localhost"
)

cur = conn.cursor()

# Fetch latest prices for each symbol
cur.execute("""
    SELECT symbol, price_usd, fetched_at
    FROM crypto_prices
    ORDER BY fetched_at DESC
""")
rows = cur.fetchall()

conn.close()

# Organize data for plotting
symbols = []
prices = []
times = []

for row in rows:
    symbols.append(row[0])
    prices.append(float(row[1]))
    times.append(row[2])

# Optional: To avoid duplicates, just get last price per symbol
# We'll make a dict: symbol -> latest price
latest_prices = {}
for symbol, price, fetched_at in rows:
    if symbol not in latest_prices or fetched_at > latest_prices[symbol][1]:
        latest_prices[symbol] = (price, fetched_at)

# Prepare data for plot
symbols = list(latest_prices.keys())
prices = [float(v[0]) for v in latest_prices.values()]

# Plot
plt.bar(symbols, prices)
plt.title('Latest Crypto Prices (USD)')
plt.xlabel('Cryptocurrency')
plt.ylabel('Price in USD')
plt.show()


#displaying the graph
plt.savefig('crypto_prices_plot.png')
print("Plot saved as crypto_prices_plot.png")
