#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

	if line[0] == "user_ptr_id" or line[0] == "id":
		continue

	if len(line) == 5:
		# 'user_ptr_id', 'reputation', 'gold', 'silver', 'bronze'
		print "{0}\t{1}\t{2}\t{3}\t{4}".format(line[0],line[1],line[2],line[3],line[4])
	else:
		# 'id', 'title', 'tagnames', 'author_id', 'body', 'node_type', 'parent_id', 'abs_parent_id', 'added_at', 'score'
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(line[0],line[1],line[2],line[3],line[5],line[6],line[7],line[8],line[9])
