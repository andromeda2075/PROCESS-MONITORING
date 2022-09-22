import monitoringone 
import repository 

new_repository=repository.SqliteRepository("base.sql")

#proceso1=module1.ProcessData1()
#proceso1.config('mousepad',10,new_repository)
#proceso1.start()

#proceso2=module1.ProcessData1()
#proceso2.config('xfce4-terminal',5,new_repository)
#proceso2.start()



process=monitoringone.MonitoringOne()
process.set_repository(new_repository)
process.add_monitored('mousepad',5)
process.add_monitored('xfce4-terminal',10)

process.start()
