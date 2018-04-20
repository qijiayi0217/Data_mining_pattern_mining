There are 4 algorithm scripts and a data set which is stored in a text file:
	Apriori_final_v2.py
	Apriori_improved.py
	Apriori_improved_v2.py
	FP-growth_v4.py
Put the adult.data.txt and all the python file at same folder.
Then run the scripts by using command line.
You can input the minimum support percentage (ex. 0.5 means 50%) and the scale of the data size (1 means the whole data set), both of which are used for analyzing the performance of each algorithm. But outputs will be incorrect if we add the scale of data size part to the Apriori_improved.py, so this is the only one which can not choose the scale of data size.

Also, I added a letter at the end of each attribute to record which column the attribute belongs to. For example, the attributes in first column will end with letter 'a' and the attributes in last column will end with letter 'o'.

Apriori_final_v2.py output:
	frequent pattern with their support 

Apriori_improved.py output:
	the frequent patterns in each sections (there are 7 sections)

Apriori_improved_v2.py output:
	frequent pattern with their support

FP-growth_v4.py output:
	frequent pattern with their support

PS: FP-growth can generate all the pattern with supports, but a very small part of patterns' supports are slightly lower than the exact one. So sometimes such pattern are removed incorrectly. But the runtime of this script is correct, so that the runtime analyzing in the report is convincing.
	