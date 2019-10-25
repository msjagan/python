import tarfile

num1 = 100
incr = 1
while num1 > 1:
	fname = 'flag_'+str(num1)+'.tar.gz'
	print(fname)
	if (fname.endswith("tar.gz")):
		tar = tarfile.open(fname, "r:gz")
		tar.extractall()
		tar.close()
	elif (fname.endswith("tar")):
		tar = tarfile.open(fname, "r:")
		tar.extractall()
		tar.close()
	num1 = num1-1
