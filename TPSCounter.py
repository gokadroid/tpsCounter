import gzip
import sys
import operator
import time

print (time.strftime("%H:%M:%S"))

fileHandle = ""
if len(sys.argv) != 2:
	print ("Usage: GZIPReader.py <Gzip FileName>")
	exit()

fileSpec = sys.argv[1].split(".")

if 'gz' in fileSpec:
	fileHandle = gzip.open(sys.argv[1], 'r')

if 'gz' not in fileSpec:
	fileHandle = open(sys.argv[1])

#this dcitionary contains all transaction per second per instance
tpsDictionary = {}
#this dictionar contains maximum transactions served by an instance
instanceDictionary = {}

tpsList = []

#split the line by spaces
lineSplitter = ' '

#find the time in log line at 5th index 
timeIndex = 4
#split the time to remove millisec
timeSplitter = "."

#find the isntance name at 10th index in log line
instanceNameIndex = 9

count = 0
#read log file line by line
for line in fileHandle:
	#strip any leading or trailing spaces
	line.strip()
	#keep a count of lines read, if needed
	count = count + 1
	#if (count < 1000 ):
		#print (line)
	#index x has time and y has commonInstanceName and decode it to ascii as file is opened in binary mode
	words = line.decode('ascii').split()
		#print (words)
	#index 0 has time, 1 has millisec
	timeString = words[timeIndex].split(timeSplitter)
	#print (time[0])
	#build the dictionary key to store data for each second for each instance
	tpsDictionaryKeyString = timeString[0]+"|"+words[instanceNameIndex]
	#build keystring for the unique instance name list
	instanceDictionaryKeyString = words[instanceNameIndex]
	#print ( keyString )
	tpsDictionary[tpsDictionaryKeyString] = tpsDictionary.get(tpsDictionaryKeyString, 0) + 1
	instanceDictionary[instanceDictionaryKeyString] =instanceDictionary.get(instanceDictionaryKeyString, 0) + 1
	#words[instanceNameIndex]
	#else:
	#	break

#for key,value in tpsDictionary.items():
#	print (key+" = ", value)
#for key, value in instanceDictionary.items():
#	print (key+" = ", value)

#max(tpsDictionary.iterkeys(), key=lambda k: tpsDictionary[k])
#myList = sorted(tpsDictionary.values())
#print ( sorted(tpsDictionary.values()))
tpsInstanceList = sorted(tpsDictionary.items(), key=lambda x:x[1])
instanceList = sorted(instanceDictionary.items(), key=lambda x:x[1])
print (instanceList )
print (count)

print (time.strftime("%H:%M:%S"))