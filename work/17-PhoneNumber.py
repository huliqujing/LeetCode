class Solution(object):
    def letterCombinations(self, digits, N):
        """
        :type digits: str
        :rtype: List[str]
        """
        teleph = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                  "7": "pqrs", "8": "tuv", "9": "wxyz"}

        d_len = len(digits)
        global digit, opt_dic
        if d_len == 0:
            return []
        elif d_len == 1:
            opts = list()
            for i in range(len(teleph[digits])):
                opts.append(teleph[digits][i])
            return opts
        else:
            L, R = 0, 1
            if N == 1:
                digit = []
                for i in range(d_len):
                    digit.append(digits[i])
                opt_dic = {digit[L]: teleph[digit[L]]}
            opt = list()
            if len(digit) > 1:
                for j in range(len(teleph[digit[R]])):
                    for i in range(len(opt_dic[digit[L]])):
                        opt.append(teleph[digit[R]][j] + opt_dic[digit[L]][i])
                        opt_dic[digit[L] + digit[R]] = opt
                digit = [digit[L] + digit[R]] + digit[R+1:]
                while len(digit) > 1:
                    N = 2
                    S = Solution()
                    S.letterCombinations(digit, N)
            return opt_dic[list(opt_dic.keys())[-1]]

S = Solution()
print(S.letterCombinations("234",1))
