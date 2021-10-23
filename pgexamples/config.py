#%%
import os
from configparser import ConfigParser

#%%
class Config():
  
  config_param_class = 'ConfigParams'

  class ConfigParam():

    def getAsDict(self):
      return self.__dict__ 
 

  def __init__(self) -> None:
    # SectionClass = type(Config.config_param_class, (), {})
    # self._params = SectionClass()
    self._params = Config.ConfigParam()
    print('Config.init: pwd =', os.getcwd())


  def __repr__(self) -> str:
    return str(self.__dict__)
    

  def load_config_file(self, filename='database.ini', section='postgresql'):
    print('cwd=', os.getcwd())
    
    parser = ConfigParser()    
    parser.read(filename)

    db = {}
    if parser.has_section(section):
      params = parser.items(section)

      for param in params:
          db[param[0]] = param[1]
          self.set(param[0],param[1], section)
    else:
      raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


  def set(self, key, value, section):    
    if not section:
      setattr(self._params, key, value)      

    if not hasattr(self._params, section):    
      # SectionClass = type(Config.config_param_class, (), { key: value })      
      # setattr(self._params, section, SectionClass())     
      setattr(self._params, section, Config.ConfigParam())     
    
    setattr(getattr(self._params, section), key, value)
    

  @property
  def params(self):
    return self._params

#%%
if __name__ == '__main__':
  config = Config()

  config.load_config_file()
  print(config.params.postgresql.host)
  print(config.params.postgresql.port)
  print(config.params.postgresql.getKWArgs())
  print(str(config) + 'aa')