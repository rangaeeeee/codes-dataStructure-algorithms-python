#!/usr/bin/python3
'''

R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.

'''

def minmax(data):
  minimum,maximum = None,None
  if data:
    minimum = data[0]
    maximum = data[0]
  for x in data[1:]:
    if x < minimum:
      minimum = x
    if x > maximum:
      maximum = x
  return {minimum,maximum}

def main():
  print("enter the list number : ")
  data = list(map(int,input().split()))
  print(minmax(data))

if __name__ == '__main__':
  main()
