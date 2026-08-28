import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_with_another_name(self):
        self.assertEqual(greet("Bob"), "Hello, Bob!")


if __name__ == "__main__":
    unittest.main()
