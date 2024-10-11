from typing import NamedTuple
import numpy as np

#used namedtuple instead of defining __init__()
#point structure, stores the x and y positions
class point(NamedTuple):
    x_pos:float
    y_pos:float


    def __str__(self):
        return "(" + str(self.x_pos) + "," + str(self.y_pos) + ")"
    
#print points
def print_points(points):
    for p in points:
        print(str(p))

#-1 is clockwise, 1 is counterclockwise
"""
finds the orientation of the points by using the slope. 
we find slope between p1 and p2, p2 and p3
if slope between p1 and p2 is greater than they are clockwise
if they are equal they are collinear
if the slope is between p2 and p3 is greater than we are counterclockwise
@param takes 3 points p1,p2,p3
@return the orientation of the points as:
-1 - clockwise
0 - collinear
1 - counterclockwise
"""
def orientation(p1,p2,p3):
    m = (p2.y_pos-p1.y_pos)*(p3.x_pos-p2.x_pos)-(p3.y_pos-p2.y_pos)*(p2.x_pos-p1.x_pos)
    return 0 if m==0 else (1 if m < 0 else -1)

"""
Finds the leftmost point by x-position
@param takes a list of points
@return the leftmost point from the set of points
"""
def get_leftmost(ps):
    idx=0
    for i in range(len(ps)):
        if ps[i].x_pos>ps[idx].x_pos:
            idx=i
    return idx


def jarvis_march(points):
    n=len(points)
    if n<3:
        return None
    
    hull=[]
    left_idx=get_leftmost(points)
    #start at leftmost point
    p=left_idx
    
    while True:
        hull.append(points[p])
        #choose random point in this case i just use the middle point 
        q=n//2
        for i in range(n):
            #if the orientation of i is more counterclockwise than q then q becomes i
            otn=orientation(points[p],points[i],points[q])
            if otn==1:
                q=i
            
        #q becomes our new leftmost point
        p=q
        #stop when we reach our initial point
        if p == left_idx:
            return hull

