import re

logfile = open('log.txt')

for line in logfile:
	line_split = line.split(',')
	if re.search(",", line):
		 print(line[line.index(','):])