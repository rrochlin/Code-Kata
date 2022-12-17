# A divide and conquer program in Python3 
# to find the smallest distance from a 
# given set of points.
import math
import copy
# A class to represent a Point in 2D plane 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
# A utility function to find the 
# distance between two points 
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * 
                     (p1.x - p2.x) +
                     (p1.y - p2.y) * 
                     (p1.y - p2.y)) 
  
# A Brute Force method to return the 
# smallest distance between two points 
# in P[] of size n
def bruteForce(P, n):
    min_val = float('inf') 
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
  
    return min_val
  
# A utility function to find the 
# distance between the closest points of 
# strip of given size. All points in 
# strip[] are sorted according to 
# y coordinate. They all have an upper 
# bound on minimum distance as d. 
# Note that this method seems to be 
# a O(n^2) method, but it's a O(n) 
# method as the inner loop runs at most 6 times
def stripClosest(strip, size, d):
      
    # Initialize the minimum distance as d 
    min_val = d 
  
     
    # Pick all points one by one and 
    # try the next points till the difference 
    # between y coordinates is smaller than d. 
    # This is a proven fact that this loop
    # runs at most 6 times 
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
  
    return min_val 
  
# A recursive function to find the 
# smallest distance. The array P contains 
# all points sorted according to x coordinate
def closestUtil(P, Q, n):
      
    # If there are 2 or 3 points, 
    # then use brute force 
    if n <= 3: 
        return bruteForce(P, n) 
  
    # Find the middle point 
    mid = n // 2
    midPoint = P[mid]
  
    #keep a copy of left and right branch
    Pl = P[:mid]
    Pr = P[mid:]
  
    # Consider the vertical line passing 
    # through the middle point calculate 
    # the smallest distance dl on left 
    # of middle point and dr on right side 
    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid) 
  
    # Find the smaller of two distances 
    d = min(dl, dr)
  
    # Build an array strip[] that contains 
    # points close (closer than d) 
    # to the line passing through the middle point 
    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n): 
        if abs(lr[i].x - midPoint.x) < d: 
            stripP.append(lr[i])
        # if abs(Q[i].x - midPoint.x) < d: 
        #     stripQ.append(Q[i])
  
    stripP.sort(key = lambda point: point.y) #<-- REQUIRED
    min_a = min(d, stripClosest(stripP, len(stripP), d)) 
    # min_b = min(d, stripClosest(stripQ, len(stripQ), d))
      
      
    # Find the self.closest points in strip. 
    # Return the minimum of d and self.closest 
    # distance is strip[] 
    return min_a
  
# The main function that finds
# the smallest distance. 
# This method mainly uses closestUtil()
def closest(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)    
  
    # Use recursive function closestUtil() 
    # to find the smallest distance 
    return closestUtil(P, Q, n)
  
# Driver code
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
correct_points = ((0.3151657134645216, 0.31387338521199193), (0.32227936174838223, 0.31313015257523047))
P_correct = [Point(*p) for p in correct_points]
answer = dist(*P_correct)
P = [Point(*p) for p in points]
# P = [Point(2, 3), Point(12, 30),
#      Point(40, 50), Point(5, 1), 
#      Point(12, 10), Point(3, 4)]
n = len(P) 
print("was it correct? :", closest(P, n) == answer)
print(answer)
  
# This code is contributed 
# by Prateek Gupta (@prateekgupta10)