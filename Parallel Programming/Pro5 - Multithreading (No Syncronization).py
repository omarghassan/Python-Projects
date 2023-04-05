#Multithreading (No Syncronization)

class race_condition:
  amount = 100

  def husband(self):
    for i in range(1000000):
      self.amount+= 10
    print("Husband Finished")

  def wife(self):
    for i in range(1000000):
      self.amount-= 10
    print("Wife Finished")

rc = race_condition()

print(rc)

Thread(target = rc.husband, args = ()).start()
Thread(target = rc.wife, args = ()).start()

time.sleep(6)

print("Current Amount = ", rc.amount)
