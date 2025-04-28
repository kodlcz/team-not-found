import unittest
from calc_lib import *

class TestMyMathLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1),2)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(-1,-1),-2)
        self.assertEqual(add(430,142),572)
        self.assertEqual(add(-436,572),136)
        self.assertEqual(add(-574,-284),-858)
    def test_sub(self):
        self.assertEqual(sub(1,1),0)
        self.assertEqual(sub(-1,1),-2)
        self.assertEqual(sub(-1,-1),0)
        self.assertEqual(sub(1,-1),2)
        self.assertEqual(sub(430,142),288)
        self.assertEqual(sub(-436,572),-1008)
        self.assertEqual(sub(-574,-284),-290)
        self.assertEqual(sub(436,-572),1008)
    def test_mul(self):
        self.assertEqual(mul(1,1),1)
        self.assertEqual(mul(-1,1),-1)
        self.assertEqual(mul(-1,-1),1)
        self.assertEqual(mul(430,142),61060)
        self.assertEqual(mul(-436,572),-249392)
        self.assertEqual(mul(-574,-284),163016)
    def test_div(self):
        self.assertEqual(div(1,1),1)
        self.assertEqual(div(-1,1),-1)
        self.assertEqual(div(-1,-1),1)
        self.assertAlmostEqual(div(430,142),430/142)
        self.assertAlmostEqual(div(-436,572),-436/572)
        self.assertAlmostEqual(div(-574,-284),574/284)
    def test_div_zero(self):
        self.assertEqual(div(14,0),"chyba_2")
if __name__ == "__main__":
    unittest.main()
