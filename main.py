import module1 
import time
import threading

process=module1.MonitoringOne()

new_repository=module1.Repository()

process.set_repository(new_repository)



# BUcle principal

name1='gnome-screenshot'
name2='bash'
def timer(timer_runs):
	while timer_runs.is_set():
		process.monitoring(name1,name2)
timer_runs=threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()
tiempo_ejecucion=10
time.sleep(tiempo_ejecucion)  # EN SEGUNDOS 
timer_runs.clear()
print('El timer fue detenido')



