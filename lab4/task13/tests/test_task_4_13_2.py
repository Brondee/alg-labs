import unittest
from lab4.task13.src.stack import Stack 

class AlgorithmsSortTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
    
    def test_should_check_success_of_stack_empty(self):
        # then
        self.assertEqual(self.stack.isEmpty(), True)
        self.assertEqual(self.stack.display(), None)

    def test_should_check_success_of_stack_push_pop(self):
        # when
        self.stack.push(10)
        # then
        self.assertEqual(self.stack.isEmpty(), False)

        # when
        popped_value = self.stack.pop()
        # then
        self.assertEqual(popped_value, 10)
        self.assertEqual(self.stack.isEmpty(), True)


if __name__ == '__main__':
    unittest.main()
