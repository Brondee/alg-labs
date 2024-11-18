from lab3.task1.src.task2 import randomized_quicksort 
import utils


def k_closest_points(arr, k):
  points = []
  for x,y in arr:
    dist = int((x**2 + y**2)**0.5)
    points.append([dist, [x,y]])
  points_sort = randomized_quicksort(points, 0, len(points) - 1)
  return [x[1] for x in points_sort[0:k]]

if __name__ == '__main__':
  data = utils.read_data('lab3/task8/textf/input.txt')
  res = k_closest_points(data[1:], data[0][1])
  utils.print_task_data(8, data, res)
