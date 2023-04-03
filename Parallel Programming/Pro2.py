
'''
Parallelization Using Process
'''
import time
from multiprocessing import Process

def cpu_bound():
  c = 0
  print("Starting ...")

  for i in range(20000):
    c+= 1
  
  print("Finished ...")


if __name__ == "__main__":
  for _ in range(5):
    p = Process(target = cpu_bound, args = ())
    p.start()
