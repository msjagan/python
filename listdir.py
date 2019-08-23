import os

lists = os.listdir('.');

extn = 'py'
txtfiles = []
for file in lists:
	if file.endswith(extn):
		txtfiles.append(file)

if len(txtfiles) == 0:
	print("There are no files that endswith xml")
else:
	print("There are", len(txtfiles), "files in the directory")
