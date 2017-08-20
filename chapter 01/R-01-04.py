#!/usr/bin/python3
'''
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

'''

def sumSquare(maxNumber):
  summation = 0
  for i in range(maxNumber):
    summation += pow(i,2)
  return summation

def main():
  print("enter the sum of square till : ")
  maxNumber = int(input())
  print(sumSquare(maxNumber))
    
if __name__ == '__main__':
  main()
