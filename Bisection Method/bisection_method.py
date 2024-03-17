# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:19:47 2024

@author: Kali Linux
"""

def bisection_method(f, a, b, K=100, tol=1e-10):
    # Check if the function has different signs at the endpoints
    if f(a) * f(b) >= 0:
        raise ValueError("Function has the same sign at the endpoints of the interval.")

    # Initialize iteration count
    iteration = 0

    # Perform iterations
    while (b - a) / 2 > tol and iteration < K:
        c = (a + b) / 2  # Compute midpoint

        # Check if c is the root
        if f(c) == 0:
            return c, iteration

        # Update interval
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
         
        # Increment iteration count
        iteration += 1

    # Compute the final approximation of the root
    root = (a + b) / 2
    return root, iteration

def main():
    # Example usage:
    import math
    
    # Define the function f
    def f(x):
        return x**4 - math.cos(x**3)
    
    # Initial interval
    a = 0
    b = 1.5
    
    #max iteration
    K = 2
    
    # Call the bisection method
    root, iteration = bisection_method(f, a, b, K)
    
    # Display the result
    print("Approximate root:", root)
    print("Number of iterations:", iteration)
if __name__=='__main__':
    main()
