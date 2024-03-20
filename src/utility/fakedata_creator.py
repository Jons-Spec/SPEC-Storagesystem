'''from db_connector import DBConnection
from db_credentials import credentials

def fake_data_from_file(connection, sql_file_path):
    cursor = connection.cursor()

    with open(sql_file_path, 'r') as sql_file:
        sql_commands = sql_file.read().split(';')

    # Execute SQL commands
    for command in sql_commands:
        if command.strip():
            cursor.execute(command)

    connection.commit()
    cursor.close()
    print("Fake data inserted successfully.")

db_file_path = 'src\\utility\\SQL\\database.sql'
data_file_path = 'src\\utility\\SQL\\fakedata.sql'
db_name = DBConnection.get_database_name_from_sql_file(db_file_path)
print("Print database name",db_name)
connection = DBConnection.get_instance(credentials, db_name)

if connection:
    fake_data_from_file(connection, data_file_path)
    DBConnection.close_instance()'''
#out comment this to create fake data run ONLY ONCE!