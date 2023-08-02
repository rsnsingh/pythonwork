try: 
	fh = open("testfile1", "r") 
	fh.write("This is my test file for exception handling!!")
except IOError: print "Error: can\'t find file or read data" 
finally: 
	print "qqError: can\'t find file or read data" 

