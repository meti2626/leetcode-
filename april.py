class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        even_count, odd_count = n // 2, n - n // 2
        even_part = self.power(4, even_count, MOD)
        odd_part = self.power(5, odd_count, MOD)
        return even_part * odd_part % MOD
    
    def power(self, x: int, n: int, MOD: int) -> int:
        if x == 0:
            return 0
        if n == 0:
            return 1
        result = self.power(x, n // 2, MOD)
        result = result * result
        if n % 2 == 1:
            return x * result % MOD
        return result % MOD
