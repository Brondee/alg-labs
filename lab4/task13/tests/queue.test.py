import unittest
from task13.src.queue import Queue 

class AlgorithmsSortTestCase(unittest.TestCase):
    
    def test_should_check_success_of_queue(self):
      queue = Queue(5)
      self.assertEqual(queue.isEmpty(), True)
      self.assertEqual(queue.peek(), None)
      self.assertEqual(queue.queue_size(), 0)

      queue.enqueue(10)
      self.assertEqual(queue.isEmpty(), False)
      self.assertEqual(queue.peek(), 10)
      self.assertEqual(queue.queue_size(), 1)

      queue.dequeue()
      self.assertEqual(queue.isEmpty(), True)
      self.assertEqual(queue.peek(), None)
      self.assertEqual(queue.queue_size(), 0)
      self.assertEqual(queue.dequeue(), 'Очередь пуста')

      queue.enqueue(10)
      queue.enqueue(20)
      queue.enqueue(30)
      queue.enqueue(40)
      queue.enqueue(50)
      self.assertEqual(queue.isFull(), True)
      self.assertEqual(queue.enqueue(60), 'Очередь переполнена')


if __name__ == '__main__':
  unittest.main()