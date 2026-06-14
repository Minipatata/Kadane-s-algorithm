import array as arr
a=arr.array('i',[2,3,-1,5,-6])
current_sum=a[0]
max_sum=a[0]
for i in range(1,len(a)):
    current_sum=max(a[i],current_sum+a[i])
    max_sum=max(max_sum,current_sum)
print(max_sum)