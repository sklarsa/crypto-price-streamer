import psycopg
import time

tables = [
    'book-COINBASE',
    'ticker-COINBASE',
    'trades-COINBASE',
]

prev_ct = 0
sleep_time = 5

print(f"waiting a few seconds ({sleep_time*2} to be exact...)")

with psycopg.connect("host=localhost port=8812 dbname=qdb user=admin password=quest sslmode=disable") as conn:
    while True:
        time.sleep(sleep_time)
        current_ct = 0
        with conn.cursor() as cur:

            for t in tables:
                cur.execute(f"SELECT count(*) FROM '{t}'")
                current_ct += cur.fetchone()[0]
            if prev_ct > 0:
                print(f"{(current_ct-prev_ct)*1.0/sleep_time} rows/sec")
            prev_ct = current_ct
