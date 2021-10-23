#%%
import os
import psycopg2
from configparser import ConfigParser

print(os.getcwd())
#%%
conn = psycopg2.connect(host='localhost', port=5432, database='movies', user='tsemach', password='postgres')
print(conn)

#%%
class Connection():  

  class ConnectionWrapper():
    def __init__(self) -> None:
      print('ConnectionWrapper: init called')

  def __init__(self) -> None:
      self._conn = None
  
  def _read_config(self, config_file: str):
    section = 'postgresql'
    
    parser = ConfigParser()
    parser.read(config_file)

    # get section, default to postgresql
    self._db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            self._db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, config_file))

    return self._db


  def connect(self, config_file: str):
    """ Connect to the PostgreSQL database server """
    self._conn = None

    try:      
      params = self._read_config(config_file)
      
      print('connecting to the PostgreSQL database using params {}... '.format(params))
      self._conn = psycopg2.connect(**params)
      print('IN CONNECT conn:', self._conn)

      return self
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)

  def conn(self):
    return self._conn

#%%
if __name__ == '__main__':
  connection = Connection()

  connection.connect('database.ini')
  print('get_dsn_parameters()', connection.conn().get_dsn_parameters())

  try:  
    curs = connection.conn().cursor()

    # execute a statement
    print('PostgreSQL database version:')
    curs.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = curs.fetchone()
    print(db_version)
        
    # close the communication with the PostgreSQL
    curs.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

  finally:
    if conn is not None:
      conn.close()
      print('Database connection closed.')

#%%