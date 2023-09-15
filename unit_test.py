import unittest
from main import main

class MyTestCase(unittest.TestCase):
    def test_my(self):
        self.assertTrue(main() < 0.99)  # 预测运行结果

if __name__ == '__main__':
    unittest.main()
