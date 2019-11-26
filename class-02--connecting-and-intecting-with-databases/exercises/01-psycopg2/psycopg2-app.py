import psycopg2
import psycopg2.extras

connection = psycopg2.connect('dbname=android user=python-playground')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS distributions')

cursor.execute('''
    CREATE TABLE distributions (
        id SERIAL PRIMARY KEY, 
        version VARCHAR NOT NULL UNIQUE, 
        codename VARCHAR NOT NULL, 
        api VARCHAR NOT NULL, 
        distribution FLOAT NOT NULL)    
''')

# Using string interpolation to compose SQL queries
cursor.execute('INSERT INTO distributions(version, codename, api, distribution) VALUES (%s, %s, %s, %s)', ('2.3.7', 'Gingerbread', '10', 0.3))

one_distribution = {
    'version': '4.0.3',
    'codename': 'Ice Cream Sandwich',
    'api': '15',
    'distribution': 0.3
}

# Using named string parameters
insert_query = 'INSERT INTO distributions(version, codename, api, distribution) VALUES (%(version)s, %(codename)s, %(api)s, %(distribution)s)'

cursor.execute(insert_query, one_distribution)

distributions = [
    ('4.1.x','Jelly Bean','16',1.2),
    ('4.2.x','Jelly Bean','17',1.5),
    ('4.3','Jelly Bean','18',0.5),
    ('4.4','KitKat','19',6.9),
    ('5.0','Lollipop','21',3),
    ('5.1','Lollipop','21',11.5),
    ('6.0','Marshmallow','23',16.9),
    ('7.0','Nougat','24',11.4),
    ('7.1','Nougat','25',7.8),
    ('8.0','Oreo','26',12.9),
    ('8.1','Oreo','27',15.4),
    ('9','Pie','28',10.4)
]

insert_query = 'INSERT INTO distributions(version, codename, api, distribution) VALUES %s'

# http://initd.org/psycopg/docs/extras.html#psycopg2.extras.execute_values
psycopg2.extras.execute_values(cursor, insert_query, distributions, template=None, page_size=100)

connection.commit()

distributions = cursor.execute('SELECT * FROM distributions;')
for d in distributions:
    print(f'Android {d.codename}({d.version}), API {d.api}, Market share {d.distribution}')

cursor.close()
connection.close()