
#bin/python3!
n=6

def util(arr,i,j):

    if i > j or n < 0:
        return 10**9

    count = n-(sum(arr[i:j+1])+(j-i))
    if count >= 0:
        return count if j+1 != len(arr) else 0
    count = 10**9

    for r in range(i,j):

        space = util(arr,i,r)+util(arr,r+1,j)
        print(r,space,i,j,count)

        if space < count:
            count = space

    return count


def wordWrap(arr):
    return util(arr,0,len(arr)-1)
        

if __name__ == "__main__":

    arr = [3,2,2,5]
    print(wordWrap(arr))


#-GFG DP Solution


INF = 2147483647
def printSolution(p, n):
    k = 0
    if p[n] == 1:
        k = 1
    else:
        k = printSolution(p, p[n] - 1) + 1
    print('Line number ', k, ': From word no. ',
                                 p[n], 'to ', n)
    return k
  
def solveWordWrap (l, n, M):

    extras = [[0 for i in range(n + 1)]
                 for i in range(n + 1)]
   
    lc = [[0 for i in range(n + 1)]
             for i in range(n + 1)]
               

    c = [0 for i in range(n + 1)]
      
    p = [0 for i in range(n + 1)]
      
   
    for i in range(n + 1):
        extras[i][i] = M - l[i - 1]
        for j in range(i + 1, n + 1):
            extras[i][j] = (extras[i][j - 1] - 
                                    l[j - 1] - 1)
                                      

    for i in range(n + 1):
        for j in range(i, n + 1):
            if extras[i][j] < 0:
                lc[i][j] = INF;
            elif j == n and extras[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = (extras[i][j] * 
                            extras[i][j])
  
    c[0] = 0
    for j in range(1, n + 1):
        c[j] = INF
        for i in range(1, j + 1):
            if (c[i - 1] != INF and 
                lc[i][j] != INF and 
                ((c[i - 1] + lc[i][j]) < c[j])):
                c[j] = c[i-1] + lc[i][j]
                p[j] = i
    printSolution(p, n)
      
l = [3, 2, 2, 5]
n = len(l)
M = 6
solveWordWrap(l, n, M)
