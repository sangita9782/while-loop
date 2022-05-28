a=int(input("enter"))
b=int(input("enter"))
sum=0
while a<=b:
    if a%2==0:
        sum=sum+a
    a=a+1
print(sum)