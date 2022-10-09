class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, base=2) + int(b, base=2)
        x = bin(x).split("0b")
        return x[1]