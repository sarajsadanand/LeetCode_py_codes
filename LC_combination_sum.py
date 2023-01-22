class Solution:
    def combinationSum(self, candidates, target: int):
        res = [] #result

        def dfs(i, cur, total): # depth for search
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

abc = Solution()
abc.combinationSum([2,3,6,7], 7)