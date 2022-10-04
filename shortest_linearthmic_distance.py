'''
Given a number of points on a plane, your task is to find two points with the 
smallest distance between them in linearithmic O(n log n) time.
Example
  1  2  3  4  5  6  7  8  9
1  
2    . A
3                . D
4                   . F       
5             . C
6              
7                . E
8    . B
9                   . G
For the plane above, the input will be:
(
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)
=> closest pair is: ((6,3),(7,4)) or ((7,4),(6,3))
(both answers are valid. You can return a list of tuples too)
The two points that are closest to each other are D and F.
Expected answer should be an array with both points in any order.
Goal
The goal is to come up with a function that can find two closest 
points for any arbitrary array of points, in a linearithmic time.
Note: Don't use math.hypot, it's too slow...
naive solution:
def closest_pair(points):
  distances = {}
  for start in points[:-1]:
    for end in points[points.index(start)+1:]:
      distances[((start[0]-end[0])**2+(start[1]-end[1])**2)**.5] = (start,end)
  shortest = min(distances.keys())
  return distances[shortest]
  O(n^2) time
'''
import random
def closest_pair(points):
  distances = {}
  n = len(points)
  for i in range(n):
    start, end = random.sample(points,2)
    distances[((start[0]-end[0])**2+(start[1]-end[1])**2)**.5] = (start,end)
  shortest = min(distances.keys())
  distances = {}
  for point in points:
    neighbors = [p for p in points if (point[0]-shortest <= p[0] <= point[0]+shortest) and (point[1]-shortest <= p[1] <= point[0]+shortest)]
    if len(neighbors) < 2:
      continue
    for start in neighbors[:-1]:
      for end in neighbors[neighbors.index(start)+1:]:
        distances[((start[0]-end[0])**2+(start[1]-end[1])**2)**.5] = (start,end)
  shortest = min(distances.keys())
  return distances[shortest]



points = (
    (2, 2), # A
    (2, 8), # B
    (5, 5), # C
    (6, 3), # D
    (6, 7), # E
    (7, 4), # F
    (7, 9)  # G
)

print(closest_pair(points) == ((6, 3), (7, 4)))
small_grid = list((a,b) for a in range(0,20) for b in range(0,20))
med_grid = list((a,b) for a in range(0,50) for b in range(0,50))
large_grid = list((a,b) for a in range(0,100) for b in range(0,100))
import time
start = time.perf_counter()
print(closest_pair(small_grid))
print(start-time.perf_counter())
start = time.perf_counter()
print(closest_pair(med_grid))
print(start - time.perf_counter())
start = time.perf_counter()
print(closest_pair(large_grid))
print(start-time.perf_counter())