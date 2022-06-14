import numpy as np
from time import process_time_ns as ns



def sort(v):
  for j in range(len(v)-1,0,-1):
    for i in range(j):
      if v[i]>v[i+1]:
        t = v[i]
        v[i]=v[i+1]
        v[i+1] = t

def main (*args):
  v =np.random.randint(1,1000,1000)
  s =sorted(v)
  r =sorted (v, reverse = True)

  n1 = ns()
  m=sort(v)
  n2=ns()

  n3=ns()
  m= sort(s)
  n4= ns()

  n5=ns()
  m = sort (r)
  n6 = ns()

  print (n2-n1)
  print (n4-n3)
  print (n6 - n5)

if __name__=='__bubble__':
  bubble()
