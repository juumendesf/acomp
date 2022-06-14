import numpy as np
from time import process_time_ns as ns




def max(v):
  m = v[0] #(1)
  for i in range(1, len(v)): #(2)
    if v[i] > m: #(3)
      m = v[i] #(4)
  return m #(5)

def main (*args):
  v = np.random.randint(1,5,9)
  s = sorted(v)
  r = sorted (v, reverse=True)

  n1 = ns()
  m = sort (v)
  n2 = ns()

  n3 = ns()
  m= sort (s)
  n4 = ns()

  n5= ns()
  m= sort (r)
  n6 = ns()

  print (n2- n1)
  print (n4 - n3)
  print (n6 - n5)
  print (v)

if __name__=='__main__':
  main()