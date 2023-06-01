# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:28:27 2023

@author: simon
"""

import time
from math import sqrt # inbuilt fucntion
from joblib import Parallel, delayed


#Serial Code
def f(i):
    
    # some computations  that take time
    x=10000
    p =1;
    for j in range(x):
        for k in range(j):
            p *= k
    
    return sqrt(i ** 2);

# Find sqrt of first n numbers
n=10;

start_time = time.time()

for i in range(n):
    f(i)

end_time = time.time()
print (end_time-start_time)


#Parallel Code
start_time = time.time()

a = Parallel(n_jobs=2)(delayed(f)(i) for i in range(n)) 

# Why we need dealyed(): https://stackoverflow.com/questions/42220458/what-does-the-delayed-function-do-when-used-with-joblib-in-python

end_time = time.time()
total_time=end_time-start_time
print(str(total_time))

start_time = time.time()

a = Parallel(n_jobs=6)(delayed(f)(i ** 2) for i in range(n)) 

end_time = time.time()
print (end_time-start_time)