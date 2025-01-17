#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime


for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		cost = data[4]
	       	weekday = datetime.strptime(data[0],"%Y-%m-%d").weekday()
		print "{0}\t{1}".format(weekday,cost)
