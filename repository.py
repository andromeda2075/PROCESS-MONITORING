import sqlite3
import time
import threading
import os
from numpy import append

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
    is_ring = False
    max_register = -1
    url_prefix = "/var/local/monitor/" # Ruta de donde se extraerà la base de datos
    
    def __init__(self,name,ring=False,max_register=-1):
        super().__init__()
        self.dbName = name
        if not os.path.exists(self.url_prefix):
            os.mkdir(self.url_prefix)
        self.con = sqlite3.connect(self.url_prefix + self.dbName, check_same_thread=False)
        self.cur = self.con.cursor()
        self.lock = threading.Semaphore()
        self.is_ring=ring
        self.max_register = max_register
        print(ring,max_register)



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
        #TODO crear el trigger cuando ring es igual a TRUE
        if self.is_ring and self.max_register>0 :
            self.cur.execute("select * from sqlite_master where type = 'trigger' and name='delete_tail'")
            if res.fetchone() is None:
                print("Trigger delete_tail no existe")
                sentence1 = "CREATE TRIGGER delete_tail AFTER INSERT ON monitored BEGIN DELETE FROM monitored where rowid < NEW.rowid-"
                sentence2= str(self.max_register)
                sentence3="; END"
                sentence=sentence1+sentence2+sentence3
                print(sentence)
                self.cur.execute(sentence)
            else:
                print("Trigger delete_tail  existe")
            

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

  


