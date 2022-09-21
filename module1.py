
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

class MonitoredProccess:
	name = ''
	pid = -1


class MonitoringOne:
	m_processList = {}
	m_repository=0


	def __init__(self):
		print('Objeto monitoring_one creado')
	
	def monitoring(self,proc):
		#print(name)
		if proc.name() in self.m_processList:
			print(proc.name(), ':  pid=', proc.pid)
			if self.m_processList[proc.name()] == -1:
				self.m_processList[proc.name()] = proc.pid
				#registrar inicio
				print ('primera registro')
			else:
				if self.m_processList[proc.name()] != proc.pid:
					print('cambio')
					self.m_processList[proc.name()] = proc.pid
					#regirar en el repositorio el cambio
			
		#else:
		#	print('no considerado')
		# Obtener los procesos de varayoc y por cada uno guaRdar el detalle
		#
		#self.m_repository.log_process_detail(name,name2)
		
	def set_repository(self,repository):
		self.m_repository=repository
		pass
		
	def add_monitored(self,name):
		if not name in self.m_processList:
			self.m_processList [name] = -1
			print(name, 'se agrega a la lista de monitoreo')
		
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
     
