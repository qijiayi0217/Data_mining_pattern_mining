a=[1,3,5,7,2,4,9,11,10,15,13,14]
j=len(a)
while j>0:
	for i in range(0,len(a)-1):
		if a[i]<a[i+1]:
			c=a[i]
			a[i]=a[i+1]
			a[i+1]=c
	j-=1
print a