class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            num=int(str(x)[::-1])
        else:
            num= int('-'+str(-1*x)[::-1])
        if (num>=2**31) | (num<=-2**31):
            return 0
        else:
            return num
