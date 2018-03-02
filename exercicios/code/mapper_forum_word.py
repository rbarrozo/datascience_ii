#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv

count = 0

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

	data = line
	
	if len(data) < 5:
		continue
	
	body = data[4].lower()

	for sp in " .,!?:;\"()<>[]#$=-/":
		body = body.replace(sp,"|")
	
	words = body.split("|")

	for item in words:
		if len(item) > 0:
			print "{0}".format(item)
