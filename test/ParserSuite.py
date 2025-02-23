import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var a <- funcwitharr([1,-2,3])
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
