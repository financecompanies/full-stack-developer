import psycopg2

connection_parameters = {
    'host': 'localhost',
    'database': 'greetings',
    'user': 'greetings',
    'password': 'greetings'
}

greetings = connection_parameters['database']
drop_statement = f'DROP TABLE IF EXISTS {greetings}'
create_statement = f'''
    CREATE TABLE {greetings} (
        id SERIAL PRIMARY KEY,
        greeting VARCHAR NOT NULL UNIQUE,
        counter INT NOT NULL
    )
    '''
conn = psycopg2.connect(**connection_parameters)
conn.autocommit = True
try:
    with conn.cursor() as cursor:
        cursor.execute(drop_statement)
        cursor.execute(create_statement)
except psycopg2.Error:
    raise SystemExit(f'Failed to setup {greetings} database.\n{sys.exc_info()}')
else:
        print(f'Successfully setup {greetings} database')
