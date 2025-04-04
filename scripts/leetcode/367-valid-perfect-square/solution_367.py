import pytest

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        found_square = False
        lower_limit = 10 ** ((len(str(num)) // 2) - 1)
        if lower_limit < 1: lower_limit = 1
        n = lower_limit
        while (n*n <= num):
            if num % n == 0:
                if n*n == num:
                    return True
            n += 1
        return False
        

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
