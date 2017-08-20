'''
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''

def multiple(n,m):
  result = False
  
  if m % n == 0:
    result = "True"
  else:
    result = "False"

  return result

def main():
  
  print("enter two integer n and m : ")  
  n,m =  map(int,(input().split()))

  print(multiple(n,m))

if __name__ == '__main__':
  main()






