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
  (2,2), 
  (2,8), 
  (5,5), 
  (6,3), 
  (6,7), 
  (7,4), 
  (7,9)  
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
      return points[0], points[0], float("inf")
  distances = {}
  for start in points[:-1]:
      for end in points[points.index(start)+1:]:
          distances[((start[0]-end[0])**2+(start[1]-end[1])**2)] = (start, end)
  shortest = min(distances.keys())
  return *distances[shortest], shortest


def closest_split_pair(points, delta):
  distances = dict({float("inf"):(None,None)})
  length = len(points)
  mp = points[length//2]
  sub_points = [p for p in points if abs(p[0]-mp[0]) < delta**.5]
  if len(sub_points) < 2:
      return(None, None, float("inf"))
  for start in sub_points[:-1]:
      for end in sub_points[sub_points.index(start)+1:len(sub_points)]:
          distances[((start[0]-end[0])**2+(start[1]-end[1])**2)] = (start, end)
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
  sorted_points = sorted(points)
  p1, p2, d1 = find_closest_pair(sorted_points)
  return (p1, p2)


points = (
    (2, 2),  
    (2, 8),  
    (5, 5),  
    (6, 3),  
    (6, 7),  
    (7, 4),  
    (7, 9)  
)



points=((0.32488644562302055, 0.4498667231693663),
          (0.12472313065469581, 0.3249621072455898),
          (0.27773675365577366, 0.40106506267264624),
          (0.16767807789184905, 0.30649578857969273),
          (0.21280650792464456, 0.41052055366711737),
          (0.32306316378149474, 0.50866072041439),
          (0.13914947015710805, 0.4172829086764686),
          (0.2648520907116914, 0.3153546860578695),
          (0.16702641593773665, 0.45668424610598174),
          (0.32227936174838223, 0.31313015257523047),
          (0.31897316556484756, 0.4057716606014752),
          (0.2325381858649009, 0.3573289406389755),
          (0.26516346491571263, 0.5073387673529792),
          (0.21697719593538617, 0.5062540017120865),
          (0.3151657134645216, 0.31387338521199193),
          (0.23334774633701097, 0.4539240983499071),
          (0.2777429513679268, 0.4639928990525486),
          (0.12970169551697558, 0.46124199124502735),
          (0.18514327035096897, 0.5088093768596404),
          (0.18614844438498634, 0.3489288414659586),
          (0.13423497492446196, 0.49232126813206656),
          (0.26932414510672054, 0.36713951914944126),
          (0.17167900786789517, 0.3960551866372059),
          (0.23344786386554767, 0.31324008832508016),
          (0.1347537515666087, 0.3501699474075267),
          (0.315730759790059, 0.36611875217310497))

print(closest_pair(points) == ((0.3151657134645216, 0.31387338521199193), (0.32227936174838223, 0.31313015257523047)))














