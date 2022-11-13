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
'''
import time

def brute_force(points):
  if len(points) < 2:
    return points[0],points[0],float("inf")
  distances = {}
  for start in points[:-1]:
    for end in points[points.index(start)+1:]:
      distances[((start[0]-end[0])**2+(start[1]-end[1])**2)**.5] = (start,end)
  shortest = min(distances.keys())
  return *distances[shortest], shortest


def closest_split_pair(points, delta):
  distances = {}
  length = len(points)
  mp = points[length//2]
  sub_points = [p for p in points if (abs(p[0]-mp[0]) <= delta and abs(p[1]-mp[1]) <= delta)]
  if len(sub_points) < 2:
    return(None,None,float("inf"))
  for start in sub_points[:-1]:
    for end in sub_points[sub_points.index(start)+1:len(sub_points)]:
      distances[((start[0]-end[0])**2+(start[1]-end[1])**2)**.5] = (start,end)
  shortest = min(distances.keys())
  return *distances[shortest], shortest


def find_closest_pair(points):
  length = len(points)
  if length <= 3:
    return brute_force(points)
  left = points[length//2:]
  right = points[:length//2]
  p11, p12, d1 = find_closest_pair(left)
  p21, p22, d2 = find_closest_pair(right)
  if d1 == 0 or d2 == 0:
    return (p11, p12, d1) if d1 <= d2 else (p21, p22, d2)
  p1, p2, delta = ((p11, p12, d1) if d1 <= d2 else (p21, p22, d2))
  p31, p32, d3 = closest_split_pair(points, delta)
  return (p1, p2, delta) if delta <= d3 else (p31, p32, d3)


def closest_pair(points):
  p1, p2, d = find_closest_pair(sorted(points))
  return (p1,p2)



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

start = time.perf_counter()
print(closest_pair(small_grid))
print(start-time.perf_counter())
start = time.perf_counter()
print(closest_pair(med_grid))
print(start - time.perf_counter())
start = time.perf_counter()
print(closest_pair(large_grid))
print(start-time.perf_counter())