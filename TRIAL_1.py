count=0
while count<20:
    count=count+1
    user=int(input("enter number"))
    if user>0:
            print('positive number')
    elif user<0:
            print('negative number,end')
            break
    else:
            print("error")                 