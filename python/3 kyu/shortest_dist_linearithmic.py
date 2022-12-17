def brute_force(points):
    if len(points) < 2:
        return points[0], points[0], float("inf")
    distances = {}
    for start in points[:-1]:
        for end in points[points.index(start)+1:]:
            distances[((start[0]-end[0])**2+(start[1]-end[1])**2)] = (start, end)
    shortest = min(distances.keys())
    return *distances[shortest], shortest**.5

def check_closest(points, min_distance):
    min_val = min_distance
    length = len(points)
    distances = dict()
    for i in range(length):
        j = i + 1
        while j < length and (points[j][1] - points[i][1]) < min_val:
            min_val = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**.5
            distances[min_val] = (points[i],points[j])
            j += 1
    return (*distances[min_val], min_val) if min_val < min_distance else (None,None,float("inf"))


def find_closest_pair(points):
    length = len(points)
    if length <= 3:
        return brute_force(points)
    mid = length//2
    mid_point = points[mid]
    points_left = points[:mid]
    points_right = points[mid:]

    point_left_1, point_left_2, distance_left = find_closest_pair(points_left)
    point_right_1, point_right_2, distance_right = find_closest_pair(points_right)

    left = point_left_1, point_left_2, distance_left
    right = point_right_1, point_right_2, distance_right

    point_prelim_1, point_prelim_2, delta = min(left, right)
    near_middle_points = []
    new_points = points_left + points_right
    for point in new_points:
        if abs(point[0] - mid_point[0]) < delta:
            near_middle_points.append(point)
    sorted_y_points = sorted(near_middle_points, key=lambda point: point[1])
    pprint(sorted_y_points)
    point_final_1, point_final_2, delta_final = check_closest(sorted_y_points, delta)
    print(min(delta,delta_final))
    return (point_final_1, point_final_2, delta_final) if delta_final < delta else (point_prelim_1, point_prelim_2, delta)



def closest_pair(points):
    points = sorted(points)
    p1, p2, _ = find_closest_pair(points)
    return (p1, p2)
from pprint import pprint
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
