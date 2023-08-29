class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            if x == y:
                return True
            else:
                return False
        elif x < 0:
            if x == y:
                return True
            else:
                return False
        elif x == 0:
            return True
x =int(input())
y = int(str(x)[::-1])
z=Solution()
print(z.isPalindrome(x))