class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        コンボ = []
        マップ = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def 見つける(インデックス, コンビネーション):
            if インデックス == len(digits):
                コンボ.append(コンビネーション)
                return
            for 文字 in マップ[digits[インデックス]]:
                見つける(インデックス + 1, コンビネーション + 文字)

        見つける(0,"")

        return コンボ


print(Solution.letterCombinations(True, "23"))