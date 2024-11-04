def count_interval(data):
  s, p = data[0][0], data[0][1]
  intervals = [x for x in data[1:1+s]]
  points = data[-1]

  coordinates = []
  result = {}

  for st, end in intervals:
    coordinates.append([st, "L"])
    coordinates.append([end, "R"])
  
  for point in points:
    coordinates.append([point, "P"])
    result[point] = 0

  coordinates.sort()

  active = 0
  for pos, coord_type in coordinates:
    if coord_type == "L":
      active += 1
    elif coord_type == "R":
      active -= 1
    elif coord_type == "P":
      result[pos] = active

  return [result[point] for point in points]

if __name__ == '__main__':
  count_interval()
