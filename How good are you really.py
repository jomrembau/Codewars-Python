def better_than_average(class_points, your_points):
    if (sum(class_points) / len(class_points)) >= your_points:
        return False
    else:
        return True

print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))