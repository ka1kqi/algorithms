import random as rand
import math

def in_circle(x, y, r):
    return x*x + y*y <= r*r

def monte_carlo(n,r):
    ct = 0
    for i in range(n):
        x_pos = rand.uniform(0,1)
        y_pos = rand.uniform(0,1)
        
        if in_circle(x_pos,y_pos,r):
            ct += 1
    
    return 4*ct/n 

pi = monte_carlo(100000000,1)
err = (pi - math.pi) / math.pi
print("PI estimate: "+ str(pi))
print("Percent error: " + str(err))