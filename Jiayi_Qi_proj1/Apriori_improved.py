import datetime


print "minimum support (ex. input 0.5 for 50 %):"
min1=input()
#print "scale of data set (ex. input 0.5 for 50%):"
#scale=input()
#min_support=32561*min1
begin=datetime.datetime.now()
f=open(r'./adult.data.txt')
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
list5=list4[:]
for i in range(0,len(list5)):
	for j in range(0,len(list5[i])):
		if list5[i][j][0]==" ":
			list5[i][j]=list5[i][j][1:]
#list5=list5[:int(32561*scale)]
#po=len(list5)/7
list20=[]
list20.append(list5[0:5000])
list20.append(list5[5000:10000])
list20.append(list5[10000:15000])
list20.append(list5[15000:20000])
list20.append(list5[20000:25000])
list20.append(list5[25000:30000])
list20.append(list5[30000:])

def Apriori(list5,result,min_support):	
	store=[]
	dict1={}
	for i in range(0,len(list5)):
		for j in range(0,len(list5[i])):
			if dict1.has_key(list5[i][j]):
				dict1[list5[i][j]]+=1
			else:
				dict1[list5[i][j]]=1
	for key in dict1:
		if dict1[key]<min_support:
			store.append(key)
	for i in range(0,len(store)):
		del dict1[store[i]]
	if dict1!={}:
		for key in dict1:
			result.append(key)
	#dict1 is dictionary the 1-length frequent itemsets with support

	#using dict1 to prune the original dataset
	'''
	for i in range(0,len(list5)):
		mid=[]
		for j in range(0,len(list5[i])):
			if not dict1.has_key(list5[i][j]):
				mid.append(list5[i][j])
		for n in range(0,len(mid)):
			list5[i].remove(mid[n])
		'''
	#print list5

	#now list5 is the pruned dataset
	list7=[]
	for key in dict1:
		list7.append(key)

	#the join step
	can2=[]   #2-lenght candidate itemset
	for i in range(0,len(list7)):
		for j in range(i+1,len(list7)):
			can2.append([list7[i],list7[j]])

	#print mid
	#calculate support
	dict2={}
	#print list5
	for i in range(0,len(can2)):
		for j in range(0,len(list5)):
			if can2[i][0] in list5[j]:
				if can2[i][1] in list5[j]:
					if dict2.has_key(can2[i][0]+','+can2[i][1]):
						dict2[can2[i][0]+','+can2[i][1]]+=1
					else:
						dict2[can2[i][0]+','+can2[i][1]]=1
	#print dict2
	#dict2 is the dictionary of 2-length itemset with supports
	can2=[]
	for key in dict2:
		can2.append(key)
	#print can2
	#the prune step
	mid=[]
	for key in dict2:
		if dict2[key]<min_support:
			mid.append(key)
	for i in range(0,len(mid)):
		del dict2[mid[i]]
	if dict2!={}:
		for key in dict2:
			result.append(key)
	can3=[]

	can3.append(can2)
	can_3=[]
	#print can3
	for p in range(0,14):
		temp=[]
		for i in range(0,len(can3[p])):
			temp.append(can3[p][i].split(','))
		for i in range(0,len(temp)):
			for j in range(0,len(temp[i])):
				if temp[i][j][0]==' ':
					temp[i][j]=temp[i][j][1:]
		can=[]
		for i in range(0,len(temp)-1):
			for j in range(i+1,len(temp)):
				qjy=[]
				for n in range(0,len(temp[j])):
					if temp[j][n] not in temp[i]:
						qjy.append(temp[j][n])
				if len(qjy)==1:
					mid=temp[i][0:]
					mid.append(qjy[0])
					if mid not in can:
						can.append(mid)
		store=[]
		for i in range(0,len(can)):
			for j in range(i+1,len(can)):
				count=0
				for n in range(0,len(can[j])):
					if can[i][n] in can[j]:
						count+=1
				if count==len(can[j]):
					store.append(i)
		for i in store:
			can[i]=[]
		for i in range(0,len(store)):
			if [] in can:
				can.remove([])

		#print can
		qqq=[]
		for i in range(0,len(can)):
			qqq.append(','.join(can[i]))
		can3.append(qqq)
		can_3.append({})
		for i in range(0,len(can)):
			for j in range(0,len(list5)):
				count=0
				for n in range(0,len(can[i])):
					if can[i][n] in list5[j]:
						count+=1
				if count==len(can[i]):
					temp=','.join(can[i])
					if can_3[p].has_key(temp):
						can_3[p][temp]+=1
					else:
						can_3[p][temp]=1

		mid=[]
		for i in can_3[p]:
			if can_3[p][i]<min_support:
				mid.append(i)
		for i in range(0,len(mid)):
			del can_3[p][mid[i]]
		if can_3[p]!={}:
			for key in can_3[p]:
				result.append(key)
		else:
			break

#min_support=min1*32561
the=[]
for i in range(len(list20)):
	result=[]
	min_support=min1*len(list20[i])
	Apriori(list20[i],result,min_support)
	the.append(result)
temp=[]
dict123={}
for i in range(0,len(the)):
	for j in range(0,len(the[i])):
		temp=the[i][j].split(',')
		test=0
		for key in dict123:
			if len(temp)==len(key):
				count=0
				for n in range(0,len(temp)):
					if temp[n] in key:
						count+=1
				if count==len(key):
					dict123[key]+=1
					test=1
					break
		if test==0:
			dict123[tuple(temp)]=1
print dict123




end=datetime.datetime.now()
print 'Runtime: '+ str(end-begin)+' s'
