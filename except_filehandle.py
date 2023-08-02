import sys
inputFileOK = False
while (inputFileOK == False):
   try:
      inputFileName = input("Enter name of input file: ")
      inputFile = open(inputFileName, "r")
   except IOError:
      print("File", inputFileName, "could not be opened")
   else:
      print("Opening file", inputFileName, " for reading.")
      inputFileOK = True

      for line in inputFile:
         sys.stdout.write(line)
      print ("Completed reading of file", inputFileName)
      inputFile.close()
      print ("Closed file", inputFileName)
