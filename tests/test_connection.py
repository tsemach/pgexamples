import os
import unittest
from pgexamples.config import Config
from pgexamples.connection import Connection

class TestConnection(unittest.TestCase):
  """Connection class test"""

  def test_connect(self):
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


if __name__ == '__main__':
  unittest.main()
