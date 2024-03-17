# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:03:26 2024

@author: Kali Linux
"""

import numpy as np
import math

def Newtons_Method(f, df, x0, tol=1e-10, K=100):
    x = x0
    
    for k in range(K):
        fx = f(x)
        dfx = df(x)
        
        x_new = x - fx / dfx
        
        if np.abs(fx) < tol:
            return x_new, k
        
        x = x_new
        
    return x_new, K

def main():
    def f(x):
       return x**4 - math.cos(x**3) 
   
    def df(x):
        return 3*x**2*math.sin(x**3) + (4*x**3)
    x0 = 0.01
    
    result, iterations = Newtons_Method(f, df, x0)
    print('Fixed point:', result)
    print('Number of iterations:', iterations)
    
if __name__ == '__main__':
    main()
        
    