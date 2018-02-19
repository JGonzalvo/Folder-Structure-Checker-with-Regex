import re
import os
import shutil
import time

root=os.path.dirname(os.path.abspath(__file__))
#creating a dynamic link
lib = root + '\\lib\\'
patternLocation = lib + 'patterns.txt'

#boolean variable that monitors filter
filter=0

#filter tag
filterComment=""

def remove(pattern):
#load input and output files
	f = open('dir_list.txt')
	fo = open('output.txt','w')
		
	#match regex and write output
	for line in f:
		if (re.sub(pattern,"", line)=="") or (re.sub(pattern,"", line)=="\n"):
			print("Match Found")
		else:
			fo.write(line)
	f.close()
	fo.close()
	os.remove("dir_list.txt")
	shutil.move("output.txt","dir_list.txt")
	
def move(pattern):
	# load input and output files
	f = open('dir_list.txt')
	fo = open('output.txt','w')
	fi = open(filterComment,'w')
	
	# match regex and write output
	for line in f:
		if re.sub(pattern,"match", line)!="match":
			fo.write(line)
		else:
			fi.write(line)
	f.close()
	fo.close()
	fi.close()
	os.remove("dir_list.txt")
	shutil.move("output.txt","dir_list.txt")
	
patterns = open(patternLocation)
#line = line.replace("\n", "")
for pattern in patterns:
	if filter==1:
		pattern = re.compile(pattern, re.IGNORECASE)
		move(pattern)
		filter=0
	elif pattern[0]=='#':
		filter=1
		filterComment=pattern[1:]
		filterComment=filterComment[:-1]
		print("Filtering All ") + filterComment
		filterComment+='.txt'
	else:
		pattern = re.compile(pattern, re.IGNORECASE)
		remove(pattern)
		print("Removing Pattern Matches")

shutil.move("dir_list.txt","Other_Errors.txt")
#wait = raw_input('Press <ENTER> to continue')

		


	
	
