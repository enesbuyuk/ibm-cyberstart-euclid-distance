# 1. Define the points
points = [(1, 2), (4, 6), (7, 1), (2, 3), (5, 5)]

# 2. For Euclid distance
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# 3. Calculate the distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Find the minimum distance
min_distance = min(distances) if distances else None

print(min_distance)
