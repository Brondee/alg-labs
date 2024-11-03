from task1.src.task2 import randomized_quicksort 

def k_closest_points(arr, k):
  points = []
  for x,y in arr:
    dist = int((x**2 + y**2)**0.5)
    points.append([dist, [x,y]])
  points_sort = randomized_quicksort(points, 0, len(points) - 1)
  return [x[1] for x in points_sort[0:k]]

if __name__ == '__main__':
  k_closest_points()