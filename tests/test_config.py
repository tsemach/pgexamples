import os
import unittest
from pgexamples.config import Config

class TestConfig(unittest.TestCase):
  """config class test"""

  def test_load_config_file(self):
    print('pwd', os.getcwd())      

    config = Config()
    config.load_config_file('database.ini', section='postgresql')

    assert(config._params.postgresql.host == 'localhost')
    assert(config._params.postgresql.port == '5432')
    assert(config._params.postgresql.database == 'movies')
    assert(config._params.postgresql.user == 'tsemach')
    assert(config._params.postgresql.password == 'postgres')

    # print(config._params.postgresql.port)
    # print(config._params.postgresql.getKWArgs())


  def test_set(self):  
    config = Config()

    config.set('name', 'someone', 'user')
    # assert(config.user.name == 'someone')
    assert(config.params.user.name == 'someone')
    print('getKWArgs = ', config.params.dict())
  

if __name__ == '__main__':
  unittest.main()
