import unittest

from main import *

class MyFirstTests(unittest.TestCase):

  def test_hello(self):
    """Test to print out 'Hello World'"""
    self.assertEqual(process(), "Hello World")

  def test_logger(self):
    """Test to check if logger is working"""
    self.assertEqual(logger.warning("Running Process function"), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
