class Solution:
    def intToRoman(self, num: int) -> str:
        l1 = {1000: "M", 900: "CM", 500: "D", 400: "CD",  100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        l2 = []
        for value, symbol in l1.items():
            while num >= value:
                l2.append(symbol)
                num -= value
        return "".join(l2)
