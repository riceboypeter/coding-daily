class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        strs = sorted(strs) # massive brain IQ play here
        common = ""
        for index in range(len(strs[0])):
            try:
                if strs[0][index] == strs[-1][index]:
                    common += strs[0][index]
                else:
                    break
            except:
                break

        return common if len(strs) > 1 else strs[0]



print(Solution.longestCommonPrefix(["ab",'a']))