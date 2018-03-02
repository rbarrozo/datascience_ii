#!/usr/bin/python

import sys

oldKey = None
salesTotal = 0
salesCount = 0
salesMean = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    	data_mapped = line.strip().split("\t")
    	if len(data_mapped) != 2:
        	# Something has gone wrong. Skip this line.
		continue
	thisItem, thisSale = data_mapped

	if oldKey and oldKey != thisItem:
        	print oldKey, "\t", salesTotal 
        	
		oldKey = thisItem
        	salesTotal = 0

	oldKey = thisItem
    	salesTotal += float(thisSale)
	
if oldKey != None:
	print oldKey, "\t", salesTotal


