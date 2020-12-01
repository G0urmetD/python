import fnmatch
import os

rootPath = '/'
images = ['*.jpg', '*.png', '*.jpeg',]
matches = []

for root, dirnames, filenames in os.walk("C:\"):
	for extensions in images:
		for filename in fnmatch.filter(filenames, extensions):
			matches.append(os.path.join(root, filename))