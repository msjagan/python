import os
from os.path import join, getsize
path = input('Enter the path: ')
for root, dirs, files in os.walk(path):
	for name in files:
		print(name, "Consumes", getsize(join(root,name)), "Bytes")
	print(len(files))


