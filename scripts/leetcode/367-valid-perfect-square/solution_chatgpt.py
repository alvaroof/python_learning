class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    

if __name__ == "__main__":
    num = 9    
    solution = Solution()
    answer = solution.isPerfectSquare(num)
    print(answer)

    num = 14
    solution = Solution()
    answer = solution.isPerfectSquare(num)
    print(answer)

    num = 16
    solution = Solution()
    answer = solution.isPerfectSquare(num)
    print(answer)
        