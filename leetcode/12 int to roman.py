ref = {1:"I",
       4:"IV",
       5:"V",
       9:"IX",
       10:"X",
       40:"XL",
       50:"L",
       90:"XC",
       100:"C",
       400:"CD",
       500:"D",
       900:"CM",
       1000:"M"}

num = 3749

roman = ""

for key in dict(reversed(list(ref.items()))):
    while num >= key:
        num -= key
        roman += ref[key]

print(roman)