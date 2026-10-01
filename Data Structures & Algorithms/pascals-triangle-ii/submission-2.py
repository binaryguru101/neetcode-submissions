class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #dp[i] is the pascal numbers for index i 
        #dp[0] is [1]
        #dp[1] is [1,1]
        #dp[i] is 1 + sum of adjacent numbers + 1
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
        for i in range(1,rowIndex+1):
            newarr = adjacent_sum(dp[i-1])
            dp.append(newarr)
        return dp[-1]


        