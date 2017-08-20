'''

R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.

'''
def isEven(number):
  result = False
  if not number & 0x1:
    result = 'True'
  return result

def main():
  print("enter a number : ")
  k = int(input())
  print("entered number is even : " + str(isEven(k)))


if __name__ == '__main__':
  main()
