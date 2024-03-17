# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:43:05 2024

@author: Kali Linux
"""

def Bisection_Method(f, tol=1e-10, K=100):
    # Initialize iteration count
    iteration = 0
    
    a, b = None, None
    
    # Compute intervals
    for k in range(K):
        if f(k) < 0 and f(k+1) > 0:
            a = k
            b = k+1
            break
    print(f"The intervals are: [a, b] = {[a, b]}\n")
          
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
    
    # Call the bisection method
    root, iteration = Bisection_Method(f)
    
    # Display the result
    print("Approximate root:", root)
    print("Number of iterations:", iteration)

if __name__ == '__main__':
    main()
