def square(n):
    magic_squre =[[0 for x in range(n)] for y in range(n)]
    i = n/2
    j = n-1
    num = 1
    while num<=(n*n):
        if i==-1 and j==n:
            j = n-2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        if magic_squre[int(i)][int(j)]: # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magic_squre [int(i)][int(j)] = num
            num =num + 1
        j = j + 1
        i = i - 1
    print("magic square for n=",n)
    print("sum of each row or column", n*(n*n + 1) / 2, "\n")
    for i in range (0,n):
        for j in range (0,n):
            print('%2d ' % (magic_squre[i][j]),end = '')
            if j == n - 1:
                print()
n=int(input("Number of rows of the Magic Square:"))
square(n)
                
        
