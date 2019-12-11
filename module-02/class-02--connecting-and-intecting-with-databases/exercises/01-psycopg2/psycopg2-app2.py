import psycopg2
import psycopg2.extras

connection = psycopg2.connect('dbname=android user=python-playground')
cursor = connection.cursor()

select_all_query = 'SELECT * FROM distributions'
cursor.execute(select_all_query)
everything = cursor.fetchall()
for i in everything:
    print('from everything ->', i)

one = cursor.fetchone()
print('just one ->', one)

fetchall_5 = cursor.fetchmany(5)
for i in fetchall_5:
    print('from fetch 5 ->', i)

cursor.close()
connection.close()