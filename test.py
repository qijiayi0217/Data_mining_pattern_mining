import datetime

begin=datetime.datetime.now()
sum=0
for i in range(10000):
	for j in range(10000):
		sum=sum+1
end=datetime.datetime.now()
print end-begin




#print minute1+':'+second1
#print minute2+':'+second2

