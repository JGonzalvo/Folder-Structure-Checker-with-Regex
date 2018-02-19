import os

root="\\\\172.20.6.164\\Customer_Submissions\\ATSS\\2016"


f = open('dir_list.txt','w')

for path, subdirs, files in os.walk(root):
	for subdir in subdirs:
		#print os.path.join(path, subdir)
		f.write(os.path.join(path, subdir))
		f.write('\n')	
	for name in files:
		#print os.path.join(path, name)
		f.write(os.path.join(path, name))
		f.write('\n')	
		
			
f.close()