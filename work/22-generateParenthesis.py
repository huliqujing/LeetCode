class Solution:
    def generateParenthesis(self, n):
        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left: return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return

            dfs(paths + '(', left + 1, right)  # 生成一个就加一个
            dfs(paths + ')', left, right + 1)

        dfs('(', 1, 0) ## 给定二叉树的顶层初值 "(", 因此 left 为 1
        return res
