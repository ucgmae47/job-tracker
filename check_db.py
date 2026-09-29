import psycopg

conn_string = "postgresql://jobtracker:devpassword@localhost:5432/jobtracker"

with psycopg.connect(conn_string) as conn:

    with conn.cursor() as cur:

        cur.execute("SELECT * FROM applications;")

        for row in cur:
            
            print(row)
