i=100
sum_even=0
sum_odd=0
while i<=500:
    if i%2==0:
        sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i
    i=i+1
print(sum_even)
print(sum_odd)