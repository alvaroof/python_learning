# test_solution.py
from solution_367 import Solution

def test_perfect_square_true():
    s = Solution()
    assert s.isPerfectSquare(9) == True
    assert s.isPerfectSquare(16) == True
    assert s.isPerfectSquare(1) == True
    assert s.isPerfectSquare(10000) == True

def test_perfect_square_false():
    s = Solution()
    assert s.isPerfectSquare(14) == False
    assert s.isPerfectSquare(2) == False
    assert s.isPerfectSquare(9999) == False
