import psycopg2

try:
    conn=psycopg2.connect("dbname='postgres' user='postgres' password='postgres' host='localhost' port='5433'")
except:
    print ("I am unable to connect to the database.")
#with self.con as cursor:
#    cursor.execute(open("C:/Users/BerengerKoffi/Downloads/pagila-schema.sql", "r").read())
#try conn=psycopg2.connect("")