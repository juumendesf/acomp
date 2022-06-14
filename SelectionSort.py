import numpy as np
from time import process_time_ns as ns 

def sort(v):
  for j in range(len(v)-1,0,-1): #(1)
    i=0 #(2)
    for m in range(1,j+1): #(3)
      if v[m]>v[i]: #(4)
        i = m #(5)
        t = v[j] #(6)
        v[j] = v[i] #(7)
        v[i] = t #(8)

def main (*args):
  v = np.random.randint(1, 10000, 10000)
  s = sorted(v)
  r = sorted(v , reverse=True)

  n1 = ns()
  m = sort(s)
  n2 = ns()

  n3 = ns()
  m = sort(v)
  n4 = ns()

  n5 = ns()
  m = sort(r)
  n6 = ns()

  print(n2-n1)
  print(n4-n3)
  print(n6-n5)


if __name__=='__SelectionSort__':
  SelectionSort()