def is_similar(trian1, trian2):
  # for i in range(3):
  #   print(trian1[i], trian1[(i + 1) % 3], get_distance(trian1[i], trian1[(i + 1) % 3]) )
  sides1 = [get_distance(trian1[i], trian1[(i + 1) % 3]) for i in range(3)]
  sides2 = [get_distance(trian2[i], trian2[(i + 1) % 3]) for i in range(3)]

  return all(side1 / side2 == sides1[0] / sides2[0] for side1, side2 in zip(sides1, sides2))

def get_distance(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


trian1 = [(0, 0), (1, 2), (2, 0)]
trian2 = [(3, 0), (4, 2), (5, 0)]

print(is_similar(trian1, trian2))