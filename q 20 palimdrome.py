a=int(input("enter"))
p=a
rev=0
while p>0:
    z=p%10
    p=p//10
    rev=(rev*10)+z
    print(rev)
if a==rev:
    print("palimdrome")
else:
    print("nor palimdrome")