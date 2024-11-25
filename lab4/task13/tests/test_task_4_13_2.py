import unittest
from lab4.task13.src.stack import Stack 

class AlgorithmsSortTestCase(unittest.TestCase):

    def setUp(self):
      self.stack = Stack()
    
    def test_should_check_success_of_stack_empty(self):
      self.assertEqual(self.stack.isEmpty(), True)
      self.assertEqual(self.stack.display(), None)

    def test_should_check_success_of_stack_push_pop(self):
      self.stack.push(10)
      self.assertEqual(self.stack.isEmpty(), False)
      self.assertEqual(self.stack.pop(), 10)
      self.assertEqual(self.stack.isEmpty(), True)


if __name__ == '__main__':
  unittest.main()