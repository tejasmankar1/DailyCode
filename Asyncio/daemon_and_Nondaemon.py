############## Daemon Thread ##################
import threading
import  time

def monitor_temp():
    print("Monitoring tea temperature")
    time.sleep(2)

t = threading.Thread(target=monitor_temp, daemon=True)
t.start()
print("Main Program done")

############ Non daemon Thread ####################
def monitor_temp():
    print("Monitoring tea temperature")
    time.sleep(2)

t = threading.Thread(target=monitor_temp)
t.start()
print("Main Program done")
