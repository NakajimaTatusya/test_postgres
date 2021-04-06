import psycopg2

# print(psycopg2.__version__)
# print(psycopg2.apilevel)


def GetConnection():
    connectionString = 'postgresql://postgres:passw0rd@192.168.1.201:9999/dvdrental'
    return psycopg2.connect(connectionString)


if __name__ == "__main__":
    print('test connect to postgresql start.')
    with GetConnection() as conn:
        with conn.cursor() as cur:
            cur.execute('select * from category')

            for row in cur:
                print(row)
