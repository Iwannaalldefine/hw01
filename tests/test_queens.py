# tests/test_queens.py
import unittest
from src.queens import solve_n_queens

class TestNQueens(unittest.TestCase):
    # 边界用例：n=1（唯一解）
    def test_n_1(self):
        self.assertEqual(len(solve_n_queens(1)), 1)
    
    # 边界用例：n=2（无解）
    def test_n_2(self):
        self.assertEqual(len(solve_n_queens(2)), 0)
    
    # 边界用例：n=3（无解）
    def test_n_3(self):
        self.assertEqual(len(solve_n_queens(3)), 0)
    
    # 正常用例：n=8（92种解）
    def test_n_8(self):
        self.assertEqual(len(solve_n_queens(8)), 92)

if __name__ == "__main__":
    unittest.main()