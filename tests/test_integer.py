try:
    import unittest2 as unittest
except:
    import unittest
from slimrr import integer

class test_integer(unittest.TestCase):
    def test_import(self):
        import slimrr
        slimrr.integer
        from slimrr import integer

    def test_count_bits(self):
        i = 0b010101
        self.assertEqual(integer.count_bits(i), 3)

if __name__ == '__main__':
    unittest.main()
