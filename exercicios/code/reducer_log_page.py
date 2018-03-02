#!/usr/bin/python

import sys

count = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 1:
        	# Something has gone wrong. Skip this line.
        	continue

	thisResource = data_mapped

	if oldKey and oldKey != thisResource:
        	print oldKey, "\t", count
        	oldKey = thisResource
        	count = 0

    	oldKey = thisResource
    	count += 1

if oldKey != None:
    print oldKey, "\t", count

