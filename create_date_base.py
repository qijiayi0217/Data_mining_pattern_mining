import sqlite3
import datetime

begin=datetime.datetime.now()

print "minimum support (ex. input 0.5 for 50 %):"
min1=input()
min_support=32561*min1
f=open(r'/Users/qijiayi/Desktop/data_mining/proj1/adult.data.txt')
a=f.read()
f.close()
space=""
list1=list(a)
list2=space.join(list1)
list3=list2.split('\n')
count=0
for i in range(0,len(list3)):
	if list3[i]=='':
		count=count+1
for i in range(0,count):
	list3.remove('')
list4=[]
for i in range(0,len(list3)):
	list4.append(list3[i].split(','))
#mark up different int attribute
for i in range(0,len(list4)):
	for check in range(0,15):
		if check == 0:
			list4[i][check]=list4[i][check]+'a'
		elif check ==1:
			list4[i][check]=list4[i][check]+'b'
		elif check ==2:
			list4[i][check]=list4[i][check]+'c'
		elif check ==3:
			list4[i][check]=list4[i][check]+'d'
		elif check ==4:
			list4[i][check]=list4[i][check]+'e'
		elif check ==5:
			list4[i][check]=list4[i][check]+'f'
		elif check ==6:
			list4[i][check]=list4[i][check]+'g'
		elif check ==7:
			list4[i][check]=list4[i][check]+'h'
		elif check ==8:
			list4[i][check]=list4[i][check]+'i'
		elif check ==9:
			list4[i][check]=list4[i][check]+'j'
		elif check ==10:
			list4[i][check]=list4[i][check]+'k'
		elif check ==11:
			list4[i][check]=list4[i][check]+'l'
		elif check ==12:
			list4[i][check]=list4[i][check]+'m'
		elif check ==13:
			list4[i][check]=list4[i][check]+'n'
		elif check ==14:
			list4[i][check]=list4[i][check]+'o'

#len(list4)=32561
#now, the data set was stored in list4 in which every element is one line from adult.data
#And every element in list4 are also a list in which each element represent an attribute for an individual
frequent_itemset=[]

#1-length candidate itemset
can1=[]
for i in range(0,15):
	can1.append({})
#	frequent_itemset.append([])

for j in range(0,15):
	for i in range(0,len(list4)):
		if can1[j].has_key(list4[i][j]):
			can1[j][list4[i][j]]=can1[j][list4[i][j]]+1
		else:
			can1[j][list4[i][j]]=1

#the prune step for 1-length

for i in range(0,15):
	temp=[]
	for j in can1[i]:
		if can1[i][j]<min_support:
			temp.append(j)
	for n in range(0,len(temp)):
		del can1[i][temp[n]]

#now, can1 is the 1-length frequent itemset with support

#storing the frequent 1-length itemset in to result
for i in range(0,15):
	for key in can1[i]:
		frequent_itemset.append([key])
count=0
for i in range(0,len(can1)):
	if can1[i]=={}:
		count+=1
while {} in can1:
	can1.remove({})

can_1={}
for i in range(0,len(can1)):
	can_1.update(can1[i])
if can_1!={}:
	print ""
	print "1-length frequent itemsets and their supports: "
	print ""
	print can_1
else:
	print "There is no frequent itemset with support "+str(min1)
#print frequent_itemset
#the join step
mid=[]
for i in range(0,len(can1)-1):   #the last attribute 
	for q in range(0,len(can1[i])):
		for n in range(1,len(can1)-i):
			for j in range(0,len(can1[i+n])):
				mid.append([can1[i].keys()[q],can1[i+n].keys()[j]])

#now, mid is a list in which elements are 2-length itemset which joined from 1-length frequent itemset

#calculate support
can2={}

for i in range(0,len(mid)):
	for j in range(0,len(list4)):
		if mid[i][0] in list4[j] and mid[i][1] in list4[j]:
			if can2.has_key(mid[i][0]+','+mid[i][1]):
				can2[mid[i][0]+','+mid[i][1]]=can2[mid[i][0]+','+mid[i][1]]+1
			else:
				can2[mid[i][0]+','+mid[i][1]]=1




#prune step for 2-length candidate set
temp=[]
for key in can2:
	if can2[key]<min_support:
		temp.append(key)
for i in range(0,len(temp)):
	del can2[temp[i]]
if can2!={}:
	print ""
	print "2-length frequent itemsets and their supports: "
	print ""
	print can2

#the join step
temp=[]
for key in can2:
	temp.append(key.split(", "))
for i in range(0,len(temp)):
	for j in range(0,len(temp[i])):
		if temp[i][j][0]==' ':
			temp[i][j]=temp[i][j][1:]


can3=[]
for i in range(0,len(temp)-1):
	for j in range(i+1,len(temp)):
		qjy=[]
		for n in range(0,len(temp[j])):
			if temp[j][n] not in temp[i]:
				qjy.append(temp[j][n])
		if len(qjy)==1:
			mid=temp[i][0:]
			mid.append(qjy[0])
			if mid not in can3:
				can3.append(mid)
			#print mid
store=[]
for i in range(0,len(can3)):
	for j in range(i+1,len(can3)):
		count=0
		for n in range(0,len(can3[j])):
			if can3[i][n] in can3[j]:
				count=count+1
		if count==len(can3[j]):
			store.append(i)
for i in store:
	can3[i]=[]
for i in range(0,len(store)):
	can3.remove([])



#now can3 is the 3 lenght candidate set without number of support
can_3=[{}]
list5=list4[:]
for i in range(0,len(list5)):
	for j in range(0,len(list5[i])):
		if list5[i][j][0]==" ":
			list5[i][j]=list5[i][j][1:]
#print list5

for i in range(0,len(can3)):
	for j in range(0,len(list5)):
		count=0
		for n in range(0,len(can3[i])):
			if can3[i][n] in list5[j]:
				count+=1
		if count==len(can3[i]):
			temp=','.join(can3[i])
			if can_3[0].has_key(temp):
				can_3[0][temp]+=1
			else:
				can_3[0][temp]=1

#print len(can_3)
#print len(can3)
#print can3
#print can_3

#The prune step
mid=[]
for i in can_3[0]:
	if can_3[0][i]<min_support:
		mid.append(i)
for i in range(0,len(mid)):
	del can_3[0][mid[i]]
if can_3[0]!={}:
	print ""
	print "3-length frequent itemsets and their supports: "
	print ""
	print can_3[0]


#now can_3 is the 3-length frequent itemset with support

#the loop for further joining and pruning
for p in range(1,13):
	temp=[]
	for key in can_3[p-1]:
		temp.append(key.split(","))
	for i in range(0,len(temp)):
		for j in range(0,len(temp[i])):
			if temp[i][j][0]==' ':
				temp[i][j]=temp[i][j][1:]


	can3=[]
	for i in range(0,len(temp)-1):
		for j in range(i+1,len(temp)):
			qjy=[]
			for n in range(0,len(temp[j])):
				if temp[j][n] not in temp[i]:
					qjy.append(temp[j][n])
			if len(qjy)==1:
				mid=temp[i][0:]
				mid.append(qjy[0])
				if mid not in can3:
					can3.append(mid)
			#print mid
	store=[]
	for i in range(0,len(can3)):
		for j in range(i+1,len(can3)):
			count=0
			for n in range(0,len(can3[j])):
				if can3[i][n] in can3[j]:
					count=count+1
			if count==len(can3[j]):
				store.append(i)
	for i in store:
		can3[i]=[]
	for i in range(0,len(store)):
		if [] in can3:
			can3.remove([])



#now can3 is the 3 lenght candidate set without number of support
	can_3.append({})
	list5=list4[:]
	for i in range(0,len(list5)):
		for j in range(0,len(list5[i])):
			if list5[i][j][0]==" ":
				list5[i][j]=list5[i][j][1:]
#print list5

	for i in range(0,len(can3)):
		for j in range(0,len(list5)):
			count=0
			for n in range(0,len(can3[i])):
				if can3[i][n] in list5[j]:
					count+=1
			if count==len(can3[i]):
				temp=','.join(can3[i])
				if can_3[p].has_key(temp):
					can_3[p][temp]+=1
				else:
					can_3[p][temp]=1

#print len(can_3)
#print len(can3)
#print can3
#print can_3

#The prune step
	mid=[]
	for i in can_3[p]:
		if can_3[p][i]<min_support:
			mid.append(i)
	for i in range(0,len(mid)):
		del can_3[p][mid[i]]
	if can_3[p]!={}:
		print ""
		print str(p+3)+"-length frequent itemsets and their supports:"
		print ""
		print can_3[p]
	else:
		break



end=datetime.datetime.now()
print 'Run time: '+ str(end-begin)+' s'
#print frequent_itemset

	
