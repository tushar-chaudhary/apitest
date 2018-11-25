import psycopg2
import csv

conn = psycopg2.connect("host='localhost' port='5432' dbname='apitest' user='root' password='tushar1997'")
cur = conn.cursor()
with open('IN.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        if(row[3] != '' and row[4] != ''):
            row.append('SRID=4326;POINT('+ row[4] +' '+ row[3] +')')
            if(row[6] != ''):
                cur.execute(
                    "INSERT INTO pincode_pincode VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    row
                )
conn.commit()
