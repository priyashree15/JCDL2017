from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)
#########################Check#################################
def corr(x,y):
	r_row, p_value = stats.pearsonr(x, y)
	return r_row

list_t10_1=[]
list_t10_2=[]
list_t10_3=[]
list_t10_4=[]
list_t10_5=[]
list_t10_6=[]

max_p1=[]
max_p2=[]
max_p3=[]
max_p4=[]
max_p5=[]
max_p6=[]

avgDist={}
with open('ccAvgD.txt','r') as f:
	for line in f:
		entry=line[:-1].split("\t")
		avgDist[entry[0]]=entry[1]

op=open("18_OCT_CC_results.txt","a")
with open("24S_CC_analysis.txt","r") as in_file:
	for line in in_file:
		try:
			entry=line[:-1].split("\t")
			# print entry
			# if len(entry)<2 or entry[1]=="":
			# 	continue
			if paperCitationCount.has_key(entry[0]) and avgDist.has_key(entry[0]) and float(avgDist[entry[0]])>=2:# and float(avgDist[entry[0]])<2:

				year=paperCitationCount[entry[0]]
				l=year.keys()
				l.sort()
				count=paperCitationCount[entry[0]][l[2]] #bucketing after 1 year
				count1 = paperCitationCount[entry[0]][l[-1]]
				# print entry[1]
				if float(entry[1])>=float(250):#and float(entry[1])<float(250):
					if count>=int(0) and count<int(5):	
						list_t10_1.append(count1)
						max_p1.append(float(entry[1]))
					# elif count>=int(5) and count<int(10):
					# 	list_t10_2.append(count1)
					# 	max_p2.append(float(entry[1]))
					# elif count>=int(10) and count<int(20):
					# 	list_t10_3.append(count1)
					# 	max_p3.append(float(entry[1]))
					# elif count>=int(20) and count<int(100):
					# 	list_t10_4.append(count1)
					# 	max_p4.append(float(entry[1]))
					# elif count>=int(100) and count<int(1000):
					# 	list_t10_5.append(count1)
					# 	max_p5.append(int(entry[3]))
					else:
						if count>=int(5): 
							list_t10_6.append(count1)
							max_p6.append(float(entry[1]))
					list_t10_5.append(count1)
					max_p5.append(float(entry[1]))
		except KeyError,e:
			continue
				# 
# op.write("Correlation Values for cc(taken mean of max publication count citer author) and citaion count after 10 years\n\n0-10:\n\n")
op.write("\nCA >=2");
op.write("\n(>=250)\n")
op.write("(0-5)\t")
op.write(str(len(max_p1)))
op.write("\t")
op.write(str(round(corr(max_p1,list_t10_1),3)))
op.write("\n")

# op.write("(5-10)\t")
# op.write(str(len(max_p2)))
# op.write("\t")
# op.write(str(round(corr(max_p2,list_t10_2),3)))
# op.write("\n")

# op.write("(10-20)\t")
# op.write(str(len(max_p3)))
# op.write("\t")
# op.write(str(round(corr(max_p3,list_t10_3),3)))
# op.write("\n")

# op.write("(20-100)\t")
# op.write(str(len(max_p4)))
# op.write("\t")
# op.write(str(round(corr(max_p4,list_t10_4),3)))
# op.write("\n")

op.write("(>=5)\t")
op.write(str(len(max_p6)))
op.write("\t")
op.write(str(round(corr(max_p6,list_t10_6),3)))
op.write("\n")

op.write("All\t")
op.write(str(len(max_p5)))
op.write("\t")
op.write(str(round(corr(max_p5,list_t10_5),3)))
op.write("\n")


