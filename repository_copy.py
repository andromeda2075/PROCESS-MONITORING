import sqlite3
import time
import threading

class Repository:
    def __init__(self):
        print('se ha creado el repositorio')
        
    def log_start_process(self,proc):
        #tiempo_inicial=datetime.fromtimestamp(proc.create_time()).strftime('%H:%M:%S')
        print(proc.name(),"se registra inicio del proceso")

    def log_running_process(self,proc):
        #tiempo_inicial=datetime.fromtimestamp(proc.create_time()).strftime('%H:%M:%S')
        print(proc.name(),"se registra consumo del proceso")

    def log_fail_process(self,name,pid):
        print(name, "se registra caida del proceso. Ultimo PID=",pid)

    def PC_process(self):
        pass
     
class SqliteRepository(Repository):
    dbName=""
    con = 0
    cur = 0
    lock = 0
    
    def __init__(self,name):
        super().__init__()
        self.dbName = name
        self.con = sqlite3.connect(self.dbName, check_same_thread=False)
        self.cur = self.con.cursor()
        self.lock = threading.Semaphore()


        res = self.cur.execute("SELECT name FROM sqlite_master WHERE name='monitored'")
        if res.fetchone() is None:
            print("monitored: tabla no existe")
            self.cur.execute("CREATE TABLE monitored(name,timestamp,event, pid, cpu, memory)")
        else:
            print("monitored: tabla existe")


        res = self.cur.execute("SELECT name FROM sqlite_master WHERE name='pc'")
        if res.fetchone() is None:
            print("pc: tabla no existe")
            self.cur.execute("CREATE TABLE pc(name,timestamp,event, pid, cpu,memory)")
        else:
            print("pc: tabla existe")
    
    def log_start_process(self,proc):
        """Método que inicia el proceso"""
        self.lock.acquire()
        data = [
            (proc.name(), proc.create_time(),"start", proc.pid,proc.cpu_percent(interval=0.5),proc.memory_percent()),
        ]
        self.cur.executemany("INSERT INTO monitored VALUES(?, ?, ?, ?, ?, ?)", data)
        self.con.commit()
        self.lock.release()
        print(proc.name(),"se registra inicio del proceso",proc.pid)

    

    def log_running_process(self,proc):
        """Método que iregitra el proceso"""
        self.lock.acquire()
        data = [
            (proc.name(), time.time(),"runnig",proc.pid, proc.cpu_percent(interval=0.1),proc.memory_percent()),
        ]
        self.cur.executemany("INSERT INTO monitored VALUES(?, ?, ?, ?, ?, ?)", data)
        self.con.commit()
        self.lock.release()
        #for row in cur.execute("SELECT name,pid")
        #print(proc.name(),"se registra consumo del proceso")
        print(proc.name()," Se registra ")

    def log_fail_process(self,name,pid):
        """Método que reporta la caida"""
        self.lock.acquire()
        data = [
            (name, time.time(),"fail",pid,0,0),
        ]
        self.cur.executemany("INSERT INTO monitored VALUES(?, ?, ?, ?, ?, ?)", data)
        self.con.commit()
        self.lock.release()
        print(name, " Registra caida del proceso. Ultimo PID=",pid)

  


