class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #dp[i] means the ith row 
        #dp[0] = [1]
        #dp[1] = [1,1]
        #dp[2] = 1 + sumof adjacent + 1 
        if numRows == 0:
            return 0
        def adjacent_sum(arr): 
            i = 0 
            j = 1
            final = [1]
            while j < len(arr):
                final.append(arr[i]+arr[j])
                i+=1
                j+=1
            final.append(1)
            return final
        dp = [[1]] 
        for i in range(1,numRows):
            new_row = adjacent_sum(dp[i-1])
            dp.append(new_row)
        return dp

        