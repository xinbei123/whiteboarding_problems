class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # without converting num to str

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # x = 1221
        # x % 10 -> 1, then tmp = x // 10 -> 122
        # tmp % 10 -> 2, then 1 * 10 + 2 = 12

        reverted = 0

        while x > reverted:
            reverted = reverted * 10 + x % 10
            x = x // 10

        return x == reverted or x == reverted / 10


        # convert num to str
        return str(x) == str(x)[::-1]