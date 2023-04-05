#Parallel

import urllib.request
import json
import time
from threading import Thread

finished_work = 0

def count_letters(url, frequencies):

  response = urllib.request.urlopen(url)
  text = str(response.read())

  for l in text:
    letter = l.lower()
    if letter in frequencies:
      frequencies[letter]+= 1
  
  global finished_work
  finished_work+= 1

def main():
  frequencies = {}

  for i in "abcdefghijklmnopqrstuvwxyz":
    frequencies[i] = 0
  
  start = time.time()
  
  #Make 20 Threads and each thread takes a web page
  for i in range(1000, 1020):
    t = Thread(target = count_letters, args = (f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequencies))

  end = time.time()
  print(json.dumps(frequencies, indent = 4))

  print("Time Taken: ", end-start)
  
main()
