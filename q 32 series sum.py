i=1
sum=0
n=int(input("enter"))
while i<=n:
    if i%2==0:
        print(i*i)
    else:
        print("-",i*i)
    i=i+1
    sum=sum+i
print(sum)