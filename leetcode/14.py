class solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        common = ""
        for i in range(n - 1):
            print(strs[i])
            m = len(strs[i])
            for j in range(m - 1):
                print(strs[i][j])
