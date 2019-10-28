
class Solution:

    # def is_int32b(self, num):
    #     if abs(n) <= 2**31-1 or abs(n) >= -2**31:
    #         return True
    #     else:
    #         return False

    def reverse(self, n: int) -> int:
        if abs(n) <= 2**31-1 or abs(n) >= -2**31:
            if n > 0:
                return int(str(n)[::-1])
            else:
                num_str = str(n)
                num_str = '-'+num_str[::-1][:-1]
                x = int(num_str)
                print(type(x))
                return x
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    n = int(input('Digite um numero: '))
    print(s.reverse(n))
