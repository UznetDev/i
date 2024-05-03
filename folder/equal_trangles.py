def are_triangles_congruent(triangle1, triangle2):
  triangle1.sort()
  triangle2.sort()
  for i in range(3):
    if distance(triangle1[i], triangle2[i]) != distance(triangle1[(i + 1) % 3], triangle2[(i + 1) % 3]) or distance(triangle1[i], triangle2[i]) != distance(triangle1[(i + 2) % 3], triangle2[(i + 2) % 3]):
      return False
  return True

def distance(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

triangle1 = [(0, 0), (1, 2), (2, 0)]
triangle2 = [(3, 0), (4, 2), (5, 0)]

print(are_triangles_congruent(triangle1, triangle2))