from bs4 import BeautifulSoup

with open('log.txt') as fl:
	source = BeautifulSoup(fl, features='html.parser')
	# bs = source.find_all('b')
	# for key, value in enumerate(bs):
	# 	print(value.text)
	print(source)