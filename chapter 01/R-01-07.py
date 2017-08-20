#!/usr/bin/python3
'''
R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.

'''

def main():
  print("sum of square of number :")
  print(sum([x*x for x in range(int(input()))if x & 0x1]))
  
if __name__ == '__main__':
  main()
