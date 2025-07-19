import psycopg2

# Connecting to  postgreSQL db
conn = psycopg2.connect(
    dbname="crypto_db",
    user="allan",
    password="78student73",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Fetch data
cur.execute("SELECT * FROM crypto_prices;")
rows = cur.fetchall()

# Display results
for row in rows:
    print(row)

cur.close()
conn.close()
