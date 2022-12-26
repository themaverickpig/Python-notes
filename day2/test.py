strs = ["flower","flow","flight"]
n = len(strs)
common = ""
for i in range(n):
    m = len(strs[i])
    for j in range(m):
        print(strs[i][j])


print(common)