#!/usr/bin/python

import sys
import csv

users = {}
user = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

        if len(line) == 5:
                # 'user_ptr_id', 'reputation', 'gold', 'silver', 'bronze'
		user = {'user_ptr_id':line[0],'reputation':line[1],'gold':line[2],'silver': line[3], 'bronze': line[4]}
		users[line[0]] = user
		
	else:
	
		if not line[3] in users:
			print line[3]

		print "\"" + users[line[3]]['user_ptr_id'] + "\"\t" + "\"A\"" \
			"\t\"" + users[line[3]]['reputation'] + "\"\t" \
			"\t\"" + users[line[3]]['gold'] + "\"\t" \
			"\t\"" + users[line[3]]['silver'] + "\"\t" \
			"\t\"" + users[line[3]]['bronze'] + "\"\t" \
			"\"" + line[3] + "\"\t" + "\"B\"" \
			"\t\"" + line[1] + "\"\t" \
			"\t\"" + line[2] + "\"\t" \
			"\t\"" + line[4] + "\"\t" \
			"\t\"" + line[5] + "\"\t" \
			"\t\"" + line[6] + "\"\t" \
			"\t\"" + line[7] + "\"\t" \
			"\t\"" + line[8] + "\"\t"
		

