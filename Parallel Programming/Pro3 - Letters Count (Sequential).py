#Sequential

import urllib.request
import json
import time

def count_letters(url, frequencies):

  response = urllib.request.urlopen(url)
  text = str(response.read())

  for l in text:
    letter = l.lower()
    if letter in frequencies:
      frequencies[letter]+= 1

def main():
  frequencies = {}

  for i in "abcdefghijklmnopqrstuvwxyz":
    frequencies[i] = 0

  for i in range(1000, 1020):
    count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequencies)

  print(json.dumps(frequencies, indent = 4))

main()
