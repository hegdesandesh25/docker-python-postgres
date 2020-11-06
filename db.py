import psycopg2
con=psycopg2.connect(
        host="172.28.1.4",
        user="postgres",
        password="postgres",
        database="stripe-example",
        port=5432
)

cur= con.cursor()
cur.execute("create table test1(ID int)")
cur.execute("insert into test1 values(2)")
print("inside python container \n")
print("------------------------------------\n")
print("contents of the table test1 are\n")
cur.execute("select * from test1")

rows=cur.fetchall()

for r in rows:
    print(r)

cur.close()

con.close()
