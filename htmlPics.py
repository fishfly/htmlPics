"""
Description: 	This is program is used for packing pictures into a html, 
				thus we can read pics much easier.

Author: 		whtcjdtc2007

Time: 			2015-1-24
"""

import sys,os

def main():
	argCount = len(sys.argv)

	if argCount < 2:
		print "Usage: python htmlPics.py path\n"
		return

	path = sys.argv[1]
	
	for i in os.listdir(path):
		subpath = path + "\\" + i
		makeHtml(subpath)

def makeHtml(subpath):

	if not os.path.isdir(subpath):
		# print subpath
		return

	if checkLastDir(subpath):
		print subpath
		
		# make html book here
		f = open(subpath + '\\pics.html','w')
		
		# html header
		f.write('<html>\n<body>\n<center>\n')
		
		# html body
		pics = os.listdir(subpath)
		for i in pics:
			f.write('<img src=\'' + i + '\'></img>\n')
		
		# html footer
		f.write('</center>\n</body>\n</html>')

		f.close()

		return

	items = os.listdir(subpath)

	for i in items:
		subsubpath = subpath + "\\" + i
		makeHtml(subsubpath)

def checkLastDir(path):
	
	items = os.listdir(path)

	for i in items:
		subpath = path + "\\" + i
		if os.path.isdir(subpath):
			return False

	return True

main()