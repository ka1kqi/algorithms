from jarvis_march2d import point
from jarvis_march2d import jarvis_march
from jarvis_march2d import print_points

points=[]
points.append(point(1,1))
points.append(point(3,5))
points.append(point(5,6))
points.append(point(4,9))
points.append(point(2,2))
points.append(point(5,9))
points.append(point(10,10))
points.append(point(15,2))

hull=jarvis_march(points)

print_points(hull)