import psycopg2

try:
    conn=psycopg2.connect("dbname='postgres' user='postgres' password='postgres' host='localhost' port='5433'")
except:
    print ("I am unable to connect to the database.")
#with self.con as cursor:
#    cursor.execute(open("C:/Users/BerengerKoffi/Downloads/pagila-schema.sql", "r").read())
#try conn=psycopg2.connect("")

connexion=conn.cursor()
connexion.execute("""create table posts (title TEXT,post TEXT)""")

connexion.execute("INSERT INTO posts (title, post) VALUES (%s, %s)", ("Good", "I\'m good."))
connexion.execute("INSERT INTO posts (title, post) VALUES (%s, %s)", ("Well", "I\'m well."))
connexion.execute("INSERT INTO posts (title, post) VALUES (%s, %s)", ("Excellent", "I\'m excellent."))
connexion.execute("INSERT INTO posts (title, post) VALUES (%s, %s)", ("Okay", "I\'m okay."))

conn.commit()
connexion.close()
conn.close()
