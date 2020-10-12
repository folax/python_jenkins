import unittest
import main
 
class MainTest(unittest.TestCase):
    def test_changeValues(self):
        self.assertEqual(main.changeValues(1, 2), "output A = [%s] B = [%s]" % ('2', '1'))
        
if __name__ == '__main__':
    unittest.main()
