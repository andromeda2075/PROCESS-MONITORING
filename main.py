import module1 
import time
import threading



import psutil    


def timer(timer_runs):
	while timer_runs.is_set():
		process.monitoring(name1,name2)




process=module1.MonitoringOne()

new_repository=module1.Repository()

process.set_repository(new_repository)



# BUcle principal

process.add_monitored('mousepad')
#process.add_monitored('bash')

while (True) :
	for proc in psutil.process_iter():
		process.monitoring(proc)
		'''
		pInfoDict=proc.as_dict(attrs=['name','pid','cpu_percent','status'])
		pInfoDict['vms'] = proc.memory_info().vms / (1024 * 1024*1024)
		pInfoDict['Start Time']=datetime.fromtimestamp(proc.create_time()).strftime('%H:%M:%S')
		listOfProcess.append(pInfoDict)
		'''
	time.sleep (1)
'''
name1='gnome-screenshot'
name2='bash'
timer_runs=threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()
tiempo_ejecucion=10
time.sleep(tiempo_ejecucion)  # EN SEGUNDOS 
timer_runs.clear()
print('El timer fue detenido')


'''