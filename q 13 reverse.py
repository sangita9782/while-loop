num=int(input("enter"))
rev=0
while 0<num:
    a=num%10
    rev=(rev*10)+a
    num=num//10
    print(rev)
