class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I":1,
            "V":5,
            "IV":4,
            "X":10,
            "IX":9,
            "L":50,
            "XL":40,
            "C":100,
            "XC":90,
            "D":500,
            "CD":400,
            "M":1000,
            "CM":900
        }
        table = dict(reversed(list(table.items())))
        total = 0
        index = 0
        while index <= len(s)-1:
            if s[index] in ["I","X","C"]:
                if s[index:index+2] in table:
                    total += table[s[index:index+2]] 
                    index += 1
                else:
                    total += table[s[index]]
            else:
                total += table[s[index]]
            index += 1

        return total
        
print(Solution.romanToInt(None, "IV"))