import datetime

begin=datetime.datetime.now()
class treeNode:
	def __init__(self,nameValue,numOccur,parentNode):
		self.name=nameValue
		self.occur=numOccur
		self.nodeLink=None
		self.parent=parentNode
		self.children={}
	def inc(self,numOccur):
		self.occur+=numOccur


def updateTree(items,inTree,count,headerTable):
	if items[0] in inTree.children:
		inTree.children[items[0]].inc(count)
	else:
		inTree.children[items[0]]=treeNode(items[0],count,inTree)
		#if headerTable=={}:
			#headerTable[items[0]]=inTree.children[items[0]]
		if not headerTable.has_key(items[0]):
			headerTable[items[0]]=inTree.children[items[0]]
		else:
			updateHeader(headerTable[items[0]],inTree.children[items[0]])
	if len(items)>1:
		updateTree(items[1::],inTree.children[items[0]],count,headerTable)
#def createheader(items,inTree):
	#if item[0] in inTree.children:
		#header=headertable(item[0])
	#else:
		#for child in inTree.children[item[0]]
def updateHeader(nodeToTest,targetNode):  #To add the target Node in the end of the link list
	while (nodeToTest.nodeLink!=None):
		nodeToTest=nodeToTest.nodeLink
	nodeToTest.nodeLink=targetNode


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
list5=list4[:]
for i in range(0,len(list5)):
	for j in range(0,len(list5[i])):
		if list5[i][j][0]==" ":
			list5[i][j]=list5[i][j][1:]
#print list5
test={}
tree={}
for j in range(0,15):
	for i in range(0,len(list5)):
		if test.has_key(list5[i][j]):
			test[list5[i][j]]+=1
		else:
			test[list5[i][j]]=1
for i in test:
	if test[i]>=min_support:
		tree[i]=test[i]
#print tree
#?????
for i in range(0,len(list5)):
	mid=[]
	for j in range(0,len(list5[i])):
		if not tree.has_key(list5[i][j]):
			mid.append(list5[i][j])
	for n in range(0,len(mid)):
		list5[i].remove(mid[n])

#now, list5 was pruned. Just remain the items which support larger than minimum support

#sort list5 by support
for i in range(0,len(list5)):
	n=len(list5[i])
	while n>0:
		for j in range(0,len(list5[i])-1):
			if tree[list5[i][j]]<tree[list5[i][j+1]]:
				c=list5[i][j]
				list5[i][j]=list5[i][j+1]
				list5[i][j+1]=c
		n-=1	

#now list5 was pruned and sorted by supports from high to low

#create FP-tree
headerTable={}
tree_root=treeNode('Null',1,None)
for i in range(0,len(list5)):
	updateTree(list5[i],tree_root,1,headerTable)

'''
for key in headerTable:
	cursor=headerTable[key]
	while cursor!=None:
		if headerTable[key]:
			print cursor.name
			print cursor.occur
			cursor=cursor.nodeLink
'''
#now, we have a FP-tree with headerTable
#print headerTable

freq_pat={}
for key in headerTable:
	#print key
	#print
	CPB=[]
	support=[]
	cursor1=headerTable[key]
	
	while cursor1.nodeLink!=None:
		q=[]
		cursor=cursor1.parent
		while cursor.name!='Null':
			q.append(cursor.name)
			cursor=cursor.parent
		CPB.append(q)
		support.append(cursor1.occur)
		#print support
		cursor1=cursor1.nodeLink
	for i in range(0,len(CPB)):
		CPB[i].reverse()
	#sort CPB by lenght using buble sorting
	bub=0
	while bub<=len(CPB):
		for i in range(0,len(CPB)-1):
			if len(CPB[i])>=len(CPB[i+1]):
				oo=CPB[i][:]
				CPB[i][:]=CPB[i+1][:]
				CPB[i+1][:]=oo[:]
				ooo=support[i]
				support[i]=support[i+1]
				support[i+1]=ooo
		bub+=1
	#print 
	print key
	print CPB

	
	for p in range(0,len(CPB)):
		for v in range(p+1,len(CPB)):
			count=0
			for l in range(0,len(CPB[p])):
				if CPB[p][l] not in CPB[v]:
					count+=1
			if count==0:
				support[p]=support[p]+support[v]
	print support
	for i in range(0,len(CPB)):
		string=','.join(CPB[i])
		string+=','+key

		if support[i]>=min_support:
			freq_pat[string]=support[i]

	

print freq_pat
#print tree

	#print support
#	print min_support
















