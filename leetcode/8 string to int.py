class Solution:
    def myAtoi(self, s: str) -> int:
        accepted = ['-','+','0123456789']
        result = ""
        for i in range(0,len(s)):
            if i == 0 and s[i] in accepted:
                if s[i] == '-':
                    result += '-'
            if s[i] in accepted[2]:
                result += s[i]
            else:
                break

        return result



def use(s):
    accepted = ['-','+','0123456789']
    result = ""
    for i in range(0,len(s)):
        if s[i] == " ":
            continue
        elif result == "" and s[i] in accepted:
            result += s[i]
        elif s[i] in accepted[2]:
            result += s[i]
        else:
            break

    if result == "":
        return 0
    elif result == "-" or result == "+":
        return 0

    if result[0] == '-':
        result = result[1:]
        result = int(result) * -1
    elif result[0] == '+':
        result = int(result[1:])

    if int(result) > 2**31-1:
        return 2**31-1
    elif int(result) < -2**31:
        return -2**31
    else:
        return int(result)

s = '-+12'
print(use(s))