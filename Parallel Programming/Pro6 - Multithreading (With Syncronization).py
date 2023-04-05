
#Multithreading (With Syncronization)

from threading import Lock
class race_condition:
  amount = 100

  mutex = Lock()

  def husband(self):
    for i in range(1000000):
      self.mutex.acquire()
      self.amount+= 10
      self.mutex.release()
    print("Husband Finished")

  def wife(self):
    for i in range(1000000):
      self.mutex.acquire()
      self.amount-= 10
      self.mutex.release()
    print("Wife Finished")

rc = race_condition()


Thread(target = rc.husband, args = ()).start()
Thread(target = rc.wife, args = ()).start()

time.sleep(6)

print("Current Amount = ", rc.amount)
