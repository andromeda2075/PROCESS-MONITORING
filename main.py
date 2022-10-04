import monitoringone 
import repository 
import json

file='config.json'

f = open(file, "r")
data = json.load(f)
db_file=data['db_file']

new_repository=repository.SqliteRepository(db_file,data['ring_base'],data['max_register'])

## ejemplo de uso de la implementacion con hilo por proceso
#proceso1=module1.ProcessData1()
#proceso1.config('mousepad',10,new_repository)
#proceso1.start()
#proceso2=module1.ProcessData1()
#proceso2.config('xfce4-terminal',5,new_repository)
#proceso2.start()

process_monitor=monitoringone.MonitoringOne()
process_monitor.set_repository(new_repository)

for process in data['process_list']:
    process_monitor.add_monitored(process['name'],process['period'],process['monitoring_children'])

process_monitor.start()
