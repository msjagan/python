import re
import hashlib 

logfile = open('hash100.txt', 'r')
out = logfile.readlines()
line = ''
newline = ''
for x in range(0,len(out)):
	line = out[x].replace('\n', '')
	line = hashlib.md5(line.encode())
	newline += line.hexdigest()

newline = hashlib.md5(newline.encode()).hexdigest()
logfile.close()
print(newline)

newfile = open('newfile.txt', 'w')
newfile.write(newline)

newfile.close()
