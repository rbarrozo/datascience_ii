#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

aumountItem = 0

for line in sys.stdin:
	data = line.strip()
	resource = None
	
	posIni = data.find("\"")
	resource = data[posIni+1:data.rfind("\"")].split(" ")[1].split("?")[0]
	if resource.endswith("/"):
		resource = resource[:-1]
	
	if  resource:
		print "{0}\t".format(resource)
