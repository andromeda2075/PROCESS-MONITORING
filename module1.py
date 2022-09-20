
import procesos_info
import saveData
'''
Nombre de un proceso: name_process
Identificador de un proceso: pid
Hora de inicio de un proceso: time_start_process
Hora de reinicio de un proceso: time_restart_process
Hora de falla de un proceso: time_failed_process
Tiempo de vida: life_time
Consumo de memoria RAM:RAM_used
Número de Subprocesos: num_subprocess

'''

class MonitoringOne:

	m_repository=0


	def __init__(self):
		print('Objeto monitoring_one creado')
	
	def monitoring(self,name1,name2):
		print('monitorenado')
		# Obtener los procesos de varayoc y por cada uno guaRdar el detalle
		self.m_repository.log_process_detail(name1,name2)
		
	def set_repository(self,repository):
		self.m_repository=repository
		pass
		
		
		
class Repository:
    
	def __init__(self):
		print('se ha creado el repositorio')
    	
	def log_start_process(self,name_process,pid):
		pass
    	
	def log_process_detail(self,name1,name2):
	
		saveData.save_data(name1,name2)
		
		
    		
    	
	def log_restart_process(self):
		pass
    	
	def PC_process(self):
		pass
     
