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

	makeHtml(path)

def makeHtml(subpath):

	if not os.path.isdir(subpath):
		# print subpath
		return

	if checkLastDir(subpath):
		print subpath

		# make html book here
		f = open(os.path.join(subpath, 'book.html'), 'w')

		# html header
		f.write('<html>\n<body>\n<center>\n')

		# html body
		try:
			pics = os.listdir(subpath)
			pics.sort(key=sortAsInt)
		except Exception, e:
			print e
			return

		for i in pics:
			f.write('<img src=\'' + i + '\'></img></br>\n')

		# html footer
		f.write('</center>\n</body>\n</html>')

		f.close()

		return

	try:
		items = os.listdir(subpath)
	except Exception, e:
		print e
		return

	for i in items:
		subsubpath = os.path.join(subpath, i)
		makeHtml(subsubpath)

def checkLastDir(path):

	try:
		items = os.listdir(path)
	except Exception, e:
		print e
		return

	for i in items:
		subpath = os.path.join(path, i)
		if os.path.isdir(subpath):
			return False

	return True

def sortAsInt(val):
	try:
		return int(val)
	except Exception as e:
		pass

main()
