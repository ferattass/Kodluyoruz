# Noktaların tanımlanması
points = [(2, 3), (5, 7), (1, 1), (8, 2), (4, 4)]

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafenin bulunması
min_distance = distances[0]
for distance in distances:
    if distance < min_distance:
        min_distance = distance

# Sonucun yazdırılması
print(f"Minimum Öklid mesafesi: {min_distance}")
