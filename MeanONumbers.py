# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:18:02 2023

@author: simon
"""

import time
import numpy as np
from multiprocessing import Process, Queue
from threading import Thread
import math

#Serial Code
n =100000000
d = np.random.rand(n)
print(d.shape)


def mean():
  #Sum using for loops. We can use inbuilt NumPy Sum opeartion for better speed.
  sum = 0
  n=d.size
  for i in range(n):
    sum +=d[i]
  #Mean
  mean = sum/n
  return mean
#Time the execution
start_time = time.time()
m = mean() # compute mean of 100MM numbers.
end_time = time.time()
print (end_time-start_time)
print(m)

#Multiprocessing COde
def mean_MP(s, e, q ):

  #Sum using for loops. We can use inbuilt NumPy Sum opeartion for better speed.
  sum = 0
  for i in range(s,e+1):
    sum +=d[i]

  #Mean
  mean = sum/(e-s+1)
  q.put(mean)
  return 

n1 = math.floor(n/2)

q = Queue() #Queues are thread and process safe. For communicating between processes and threads.

p1 = Process(target=mean_MP, args=(0, n1,q )) 
p2 = Process(target=mean_MP, args=(n1+1,n-1, q)) 


#Time the execution
start_time = time.time()

p1.start()
p2.start()

p1.join() # Wait till p1 finishes
p2.join() 

m=0;
while not q.empty():
     m += q.get()

m /= 2;
    
end_time = time.time()
print (end_time-start_time)
print(m)

#Multithread code
means = [0,0];

def mean_MT(s, e, threadNum ):

  #Sum using for loops. We can use inbuilt NumPy Sum opeartion for better speed.
  sum = 0
  for i in range(s,e+1):
    sum +=d[i]

  #Mean
  mean = sum/(e-s+1)
  means[threadNum] = mean; # means is a shared varibale between the threads

  return 

n1 = math.floor(n/2)

t1 = Thread(target=mean_MT, args=(0, n1,0 ))  # Third apram is the thread number
t2 = Thread(target=mean_MT, args=(n1+1,n-1,1)) 

#Time the execution
start_time = time.time()

t1.start()
t2.start()

t1.join() # Wait till t1 finishes
t2.join() 

m = (means[0]+means[1])/2
    
end_time = time.time()
print (end_time-start_time)
print(m)




