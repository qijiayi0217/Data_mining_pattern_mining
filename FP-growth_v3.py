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

def createtree_1(items,tree_root):
	headerTable={}
	#tree_root=treeNode('Null',1,None)
	for i in range(0,len(items)):
		updateTree(items[i],tree_root,1,headerTable)
	return headerTable


##############################
def createtree_2(key,headerTable,min_support,tree_root):
	new_headerTable={}
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
	#print CPB
	#tree_root=treeNode('Null',1,None)
	for i in range(0,len(CPB)):
		updateTree(CPB[i],tree_root,support[i],new_headerTable)
	return new_headerTable
###########################

def iterate(list11,length,key,res_list,loc):
	if length!=0:
		for i in range(loc,len(list11)):
			if list11[i] not in key:
				keyyy=list11[i]+','+key
				#if dict1[keyy]<support:
					#support=dict1[keyy]
				iterate(list11,length-1,keyyy,res_list,i+1)
	elif length==0:
		res_list.append(key)


def FP_growth(inTree,frequent,headerTable,itemsss):  #itemsss is a dictionary
	cursor=inTree
	#print inTree
	test=0
	dict5={}
	list12=[]
	#print frequent
	while 1:
		if len(cursor.children)>1:
			test=1
			break
			
		elif len(cursor.children)==1:
			for key in cursor.children:
				#print cursor.children[key]
				cursor=cursor.children[key]
		elif cursor.children=={}:
			break
		
	if test==0:    #contain a single path
		#print dict5
		#if cursor:

		while 1:
			if cursor.name=='Null':
				break
			dict5[cursor.name]=cursor.occur
			list12.append(cursor.name)
			cursor=cursor.parent
		result_1=[]
		for j in range(0,len(list12)):
			for i in range(0,len(list12)+1):
				iterate(list12,i,list12[j],result_1,j)
		#print result_1
		for element in result_1:
			support=40000
			string1=element.split(",")
			#print string1
			#print dict5
			for e in string1:
				if dict5[e]<support:
					support=dict5[e]
			itemsss[frequent+','+element]=support
			#print frequent
			#print itemsss
	elif test==1:
		for key in headerTable:
			frequent2=frequent+","+key
			#frequent2=key
			itemsss[frequent2]=headerTable[key].occur
			tree_root2=treeNode('Null',1,None)
			sjsj=createtree_2(key,headerTable,min_support,tree_root2)
			#print sjsj
			if tree_root2.children!={}:
				FP_growth(tree_root2,frequent2,sjsj,itemsss)


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
tree_root=treeNode('Null',1,None)
headerTable=createtree_1(list5,tree_root)
#print headerTable
frequent_pattern={}
for key in headerTable:
	if key !='0l':
		FP_growth(tree_root,key,headerTable,frequent_pattern)
print tree
delete=[]

for key in frequent_pattern:
	if frequent_pattern[key]<min_support:
		delete.append(key)
for i in range(0,len(delete)):
	del frequent_pattern[delete[i]]

print frequent_pattern

