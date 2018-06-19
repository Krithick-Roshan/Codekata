n=int(input())
if(n>=1 and n<=100000):
    if(n%2==1):
        print('odd')
    elif(n%2==0):
        print('even')
    else:
        pass
else:
    print('invalid')
