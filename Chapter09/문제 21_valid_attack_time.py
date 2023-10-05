
attack_start_times = [0, 3]
duration = 2

points = []
for time in attack_start_times:
    points += (time, 1),
    points += (time + duration, -1),

points.sort(key=lambda p: p[0])

pre_point = points[0][0]
level = 0        
duration = 0

for point, inc in points:
    if level > 0:
        duration += point - pre_point

    pre_point = point
    level += inc
    
print(duration)
