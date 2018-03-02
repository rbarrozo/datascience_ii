#!/usr/bin/python

import sys

salesTotal = 0
salesCount = 0
salesAmount = 0

oldKey = None

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

    thisStore, thisSale = data_mapped

    if oldKey and oldKey != thisStore:
        print oldKey, "\t", salesTotal
        oldKey = thisStore
        salesTotal = 0

    oldKey = thisStore
    if float(thisSale) > salesTotal:
	salesTotal = float(thisSale)	
    salesAmount += float(thisSale)
    salesCount += 1

if oldKey != None:
    print oldKey, "\t", salesTotal
print salesAmount, "\t", salesCount
