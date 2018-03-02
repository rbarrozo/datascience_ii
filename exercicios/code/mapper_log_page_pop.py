#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

aumountItem = 0

for line in sys.stdin:
	data = line.strip().split(" ")
	resource = None
	
	if len(data) != 10:
		continue
	
	resource = data[6]

	resource = resource.replace("http://www.the-associates.co.uk","").replace("http://the-associates.co.uk","")	

	if  resource:
		print "{0}\t".format(resource)
