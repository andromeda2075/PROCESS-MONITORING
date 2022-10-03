import monitoringone 
import repository 
import configparser

'''Archivos ini'''

config=configparser.ConfigParser()
config.read(config.ini)


bd=config.get('database','dbName')

for fields in [option for option in parser['process']]:
    name=config.get('process','field')
    periodo=config.get('process','period')


new_repository=repository.SqliteRepository(bd)




process=monitoringone.MonitoringOne()
process.set_repository(new_repository)


process.add_monitored(name,period)
process.start()
