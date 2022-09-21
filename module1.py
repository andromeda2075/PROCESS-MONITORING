
import saveData
from datetime import datetime
import string
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
		time_restar=[]
		name_process=[]
		if proc.name() in self.m_processList:
			print(proc.name(), ':  pid=', proc.pid)
			if self.m_processList[proc.name()] == -1:
				self.m_processList[proc.name()] = proc.pid
				t=datetime.fromtimestamp(proc.create_time()).strftime('%H:%M:%S')
				print ('primer registro','Tiempo de inicio ', t)

			else:
				if self.m_processList[proc.name()] != proc.pid:
					tr=datetime.fromtimestamp(proc.create_time()).strftime('%H:%M:%S')
					time_restar.append(tr)
					name_process.append(proc.name())
					print('cambio','tiempo de reinicio',tr)
					#print('cambio')
					self.m_processList[proc.name()] = proc.pid
					#regirar en el repositorio el cambio
					with open("process.txt","a") as file:
						info_process=proc.name()+' '+str(proc.pid)+' '+str(tr)+'\n'
						file.write(info_process)
				

		
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
    	
	def log_start_process(self,proc):
		#tiempo_inicial=datetime.fromtimestamp(proc.create_time()).strftime('%H:%M:%S')
		#print(tiempo_inicial)
		pass

	def log_process_detail(self,name1,name2):
	
		pass	
    	
	def log_restart_process(self):
		pass
    	
	def PC_process(self):
		pass
     
