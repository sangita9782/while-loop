a=input("enter")
l=len(a)
i=0
a_s=0
while i<l:
    k=int(a[i])
    b=k**l
    a_s=b+a_s
    print(a_s)
    i=i+1
if a_s==int(a):
    print("armstrong")
else:
    print("not armstrong")
