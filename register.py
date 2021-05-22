q = input('Do you want to register (y/n):')
if q == "y":
    print( "You Can Reg ister")
    un = input( "Username: ")
    print(un)
    fn = input( "Full Name: ")
    print(fn)
    pw = input("Password: ")
    if	len( pw)<=8 :
        print("Not valid length" )
    else:
        for c in pw:
            if	c.isdigit(): f=1
            elif c=='$' or c=='#' or c=='@': ch=1
            elif c==c.upper() :U=1
            elif c==c.lower(): l=1
            else:
                continue
            if u==1 and l==1 and f==1 and ch==1:
                login = input('Do you want to login?(y/n) ')
                if login.lower() != 'n' and login.lower() != 'y':
                    while login.lower() != 'n' or login.lower() != 'y':
                        print('Please provide valid input!')
                        login = input('Do you want to login?(y/n)')
                        if login == 'y':
                            u1 = input('Enter your usename: ')
                            p1 = input('Enter password')
                            if u1 != username and p1 != pw:
                                while u1 != username and p1 != pw:
                                    print('Enter valid username/password')
                                    u1 = input('Enter your usename: ')
                                    p1 = input('Enter password')
    
    print('Task 1: Basic Calculator')
    print('Task 2: Table generator')
    print('Task 3: Pattern generator')
    print('Choose one of the following three task:')
    tasks = int(eval(input('Choose the task you want to perform ')))
    if tasks not in range(1,4):
        while tasks not in range(1,4):
            print('Please provide a valid input!')
            tasks = int(eval('Choose the task you want to perform'))

if tasks == 1:
    a = float(input('Enter 1st number:'))
    b = float(input('Enter 2nd number:'))
    print('Choose the following operations')
    print('Enter 1 for basic addition')
    print('Enter 2 for basic subtraction')
    print('Enter 3 for basic multiplication')
    print('Enter 4 for basic division')
    ops = int(eval('Enter opreation'))
    if ops == 1:
        print(a+b)
    if ops == 2:
        print(a-b)
    if ops == 3:
        print(a*b)
    if ops == 4:
        print(a/b)    
elif tasks == 2:
    n = int(input('Enter the numger: '))
    for i in range(1,11):
        print(str(n)+' x '+str(i)+' = '+str(n*i))
    
elif tasks == 3:
    n = int(input('Enter the numger: '))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print('')

