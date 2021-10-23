#%%
import psycopg2
from config import Config


#%%
class Connection():  

  class ConnectionWrapper():

    # def __init__(self, host: str, port: int, database: str, username: str, password: str) -> None:
    def __init__(self, **params) -> None:
      print('Connection::ConnectionWrapper: init called')
      self._params = params


    def __enter__(self):      
      print('ConnectionWrapper::__enter__(): called ...')
      self._conn = psycopg2.connect(**(self._params))

      return self._conn


    def __exit__(self, type, value, traceback):
      print('ConnectionWrapper::__exist__(): called ...')
      self._conn.close()
      print('ConnectionWrapper::__exist__(): called ...', self._conn.closed)


  def __init__(self) -> None:
      self._wrapper = None  


  def connect(self, **kwargs):
    """ Connect to the PostgreSQL database server using context manager\n"""
    """ parameters: host, port, database, username, password"""
    self._wrapper = self.ConnectionWrapper(**kwargs)

    return self._wrapper

  
#%%
if __name__ == '__main__':
  config = Config()
  connection = Connection()

  config.load_config_file('database.ini')
  
  print('connect param =', type(config.params.postgresql))
  print('connect param =', config.params.postgresql.getAsDict())
  print('type of connect param =', type(config.params.postgresql.getAsDict()))    

  with connection.connect(**(config.params.postgresql.getAsDict())) as conn:
    print('main: database is connected')
    
    # execute a statement
    print('PostgreSQL database version:, conn:', conn)

    curs = conn.cursor()
    curs.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = curs.fetchone()
    print(db_version)

#   try:  
#     curs = connection.conn().cursor()

#     # execute a statement
#     print('PostgreSQL database version:')
#     curs.execute('SELECT version()')

#     # display the PostgreSQL database server version
#     db_version = curs.fetchone()
#     print(db_version)
        
#     # close the communication with the PostgreSQL
#     curs.close()
#   except (Exception, psycopg2.DatabaseError) astry:  
#     curs = connection.conn().cursor()

#     # execute a statement
#     print('PostgreSQL database version:')
#     curs.execute('SELECT version()')

#     # display the PostgreSQL database server version
#     db_version = curs.fetchone()
#     print(db_version)
        
#     # close the communication with the PostgreSQL
#     curs.close()
#   except (Exception, psycopg2.DatabaseError) as error:
#     print(error)

#   finally:
#     if conn is not None:
#       conn.close()
#       print('Database connection closed.')

# #%% error:
#     print(error)

#   finally:
#     if conn is not None:
#       conn.close()
#       print('Database connection closed.')

#%%