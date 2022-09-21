import module1 
import time
import threading
import psutil    


process=module1.MonitoringOne()

new_repository=module1.Repository()

process.set_repository(new_repository)



# BUcle principal

process.add_monitored('gnome-screenshot')
#process.add_monitored('bash')

while (True) :
	for proc in psutil.process_iter():
		process.monitoring(proc)
		#new_repository.log_start_process(proc)
	time.sleep (1)
