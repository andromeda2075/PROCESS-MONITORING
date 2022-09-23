import time
import threading
import psutil

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

class ProcessData1(threading.Thread):
	m_pid = -1
	m_timeControl = 0
	m_repository=0
	m_period=0
	m_name=""
	m_exist=False
	m_isRunning=False

	def config(self,name,period,repository):
		print('Objeto monitoring_one creado')
		self.repository = repository
		self.m_period = period
		self.m_name = name

	
	def run(self):
		self.m_isRunning=True
		event = threading.Event()
		while (self.m_isRunning):
			exist = False
			for proc in psutil.process_iter():#(['pid', 'name', 'username']):
				if proc.name() == self.m_name:
					self.m_exist = True
					exist = True
					print(proc.name(), ':  pid=', proc.pid)

					if self.m_pid == -1:
						self.m_pid = proc.pid
						self.m_timeControl = proc.create_time() + self.m_period

						#registrar inicio
						#self.m_repository.log_sart_proccess(proc)
						print ('PRIMER REGISTRO')
					else:
						if self.m_pid == proc.pid:
							if time.time()>= self.m_timeControl:
								print("registrar uso")
								self.m_timeControl = time.time() + self.m_period

						else:
							self.m_pid = proc.pid
							self.m_timeControl = proc.create_time() + self.m_period

							#self.m_repository.log_restart_process(proc)
							#regirar en el repositorio el cambio
							print('cambio')
					break
			if (not exist) and self.m_exist:
				self.m_pid = -1
				self.m_exist = False
				#registrar caida
				print ("se cayo")
			event.wait(1)

	def set_repository(self,repository):
		self.m_repository=repository
		pass


class ProcessData:
	m_pid = -1
	m_timeControl = 0
	m_processed = False
	m_period=0


class MonitoringOne(threading.Thread):
	m_monitoredList = {}
	m_repository=0
	m_isRunning=False

	def monitoring(self,proc):
		if proc.name() in self.m_monitoredList:
			monitored = self.m_monitoredList[proc.name()] 
			
			if monitored.m_pid == -1:
				monitored.m_pid = proc.pid
				monitored.m_timeControl = proc.create_time() + monitored.m_period
				#registrar inicio
				self.m_repository.log_start_process(proc)
				self.AddChildren(proc,monitored.m_period)

			else:
				if monitored.m_pid == proc.pid:
					self.AddChildren(proc,monitored.m_period)
					if time.time()>= monitored.m_timeControl:
						monitored.m_timeControl = time.time() +  monitored.m_period
						#registrar uso
						self.m_repository.log_running_process(proc)
				'''
				else:
					monitored.m_pid = proc.pid
					monitored.m_timeControl = proc.create_time() + self.m_period

					#self.m_repository.log_restart_monitored(proc)
					#regirar en el repositorio el cambio
					print('cambio')
			
				'''
			monitored.m_processed = True
			
	def run(self):
		self.m_isRunning=True
		event = threading.Event()
		while (self.m_isRunning):
			for proc in psutil.process_iter():#(['pid', 'name', 'username']):
				self.monitoring(proc)
				#if proc.name()=='sleep':

					#print(proc.parents())

			for index in self.m_monitoredList:
				monitored = self.m_monitoredList[index]
				if monitored.m_pid != -1 and monitored.m_processed == False:
					#registrar caida
					self.m_repository.log_fail_process(index,monitored.m_pid)					
					monitored.m_pid = -1
				monitored.m_processed = False
			event.wait(1)

		
	def set_repository(self,repository):
		self.m_repository=repository
		
	def add_monitored(self,name,period):
		if not name in self.m_monitoredList:
			monitored = ProcessData()
			monitored.m_pid = -1
			monitored.m_period = period
			self.m_monitoredList [name] = monitored
			print(name, 'se agrega a la lista de monitoreo')

	def AddChildren(self,proc,period):
		print(proc.name(), ' procesos hijo: ', proc.children())
		for subproc in proc.children():
			self.add_monitored(subproc.name(),period)
			#print('Se aprega un subproceso: ', subproc.name())
		
