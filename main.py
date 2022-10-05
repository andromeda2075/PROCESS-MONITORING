import process_monitor 
import repository 
import configuration

## LECTURA DE LA CONFIGUARACION DESDE UN ARCHIVO JSON
config = configuration.Configuration()

##SE CREA UN REPOSITORIO QUE GUARDA DATA EN UNA BD SQLITE
new_repository=repository.SqliteRepository(config.getDbFile(),config.isRingBase(),config.getMaxRegisters())

##SE CREA EL MONITOR DE PROCESOS
process_monitor=process_monitor.ProcessMonitor()
process_monitor.set_repository(new_repository)


##SE AGREGAN LOS PROCESOS A MONITOREAR
for process in config.getProcesses():
    process_monitor.add_monitored(process['name'],process['period'],process['monitoring_children'])

##SE INICIA EL MONITOREO
process_monitor.start()
