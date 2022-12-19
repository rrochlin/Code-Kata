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
    distances = dict({float("inf"):(None,None)})
    for i in range(length):
        j = i + 1
        while j < length and (points[j][1] - points[i][1]) < min_val:
            min_val = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**.5
            distances[min_val] = (points[i],points[j])
            j += 1
            # this somehow slows down the code by like 10x if anyone would care to explain to me whats going on i would really appreciate it
            # from my perspective all I'm adding here is a variable creation and a comparison inside the loop
            # with this inplace you don't need test = min(distances.keys()), considering this loop is never
            # supposed to run more than 6 times, does this really slow us down this much over 10,000 points?
            # potential_new_min = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**.5
            # if min_val > potential_new_min:
            #     min_val = potential_new_min
            #     distances[min_val] = (points[i],points[j])
    shortest = min(distances.keys())
    return (*distances[shortest], shortest) if shortest < min_distance else (None,None,float("inf"))


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

    point_prelim_1, point_prelim_2, delta = min(left, right, key= lambda x: x[2])
    near_middle_points = []
    new_points = points_left + points_right
    for point in new_points:
        if abs(point[0] - mid_point[0]) < delta:
            near_middle_points.append(point)
    sorted_y_points = sorted(near_middle_points, key=lambda point: point[1])
    point_final_1, point_final_2, delta_final = check_closest(sorted_y_points, delta)
    return (point_final_1, point_final_2, delta_final) if delta_final < delta else (point_prelim_1, point_prelim_2, delta)



def closest_pair(points):
    points = sorted(points)
    p1, p2, _ = find_closest_pair(points)
    return (p1, p2)


from pprint import pprint
points=((-0.08249822067231952, -0.451953041781085),
(-0.15557751914363852, -0.5317339425373653),
(-0.07953951791564312, -0.3360919399295021),
(0.11700044965271178, -0.48999366111572007),
(0.02806559744448757, -0.431738268526391),
(-0.2529079161330573, -0.5486590059143881),
(-0.16564891755025948, -0.28955465721150786),
(-0.026384357880797932, -0.5046269512599868),
(-0.08130944014680462, -0.5967213449885052),
(-0.21425944150440643, -0.37596718271184687),
(-0.3255312659535955, -0.47518754074202163),
(-0.02891420785927911, -0.25450678531461324),
(-0.017290343697531713, -0.6365181077489692),
(-0.2512204993969637, -0.5546990773701307),
(0.01734102687524311, -0.3373533380985104),
(-0.062132670208743884, -0.7196527008546495),
(-0.2729475065863412, -0.4086617135773378),
(-0.21294030806441366, -0.4735450529013745),
(0.16613892351119963, -0.42832035996465206),
(-0.08521709158976362, -0.22161345357345072),
(0.1153490784929447, -0.38773447030340813),
(-0.17906489868271963, -0.6104551508896161),
(-0.021731671499465532, -0.40150364571210884),
(0.04602579111899685, -0.57721909389155),
(-0.12926457188873836, -0.6312542625410136),
(-0.15008200193840163, -0.39397200028488494))

print(closest_pair(points))


'''
[(-0.17906489868271963, -0.6104551508896161), (-0.12926457188873836, -0.6312542625410136)] 
should equal 
[(-0.2529079161330573, -0.5486590059143881), (-0.2512204993969637, -0.5546990773701307)]
'''