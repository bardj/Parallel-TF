#Takes a bam file, converts it to bed, makes a bed file of positive starts, a bed file of negative starts, a json file of positive starts, and a json file of negative starts
#Command to run:  python makejson.py FILENAME.bam

import sys
import os

#Inputs bam file, converts to BED format
input = sys.argv[1]
bed = input.rstrip('.bam') + '.bed'
os.system('bamToBed -i  '+input+' > '+bed)



file = open(bed)
neg = open(bed.rstrip('.bed')+'.negstarts.bed','w')
pos = open(bed.rstrip('.bed')+'.posstarts.bed','w')


for line in file:
	line = line.rstrip()
	a = line.split('\t')
	if a[5] == '+':
		pos.write(a[0]+ ' ' + str((int(a[1]))-5))
		pos.write('\n')
	else:
		neg.write(a[0]+ ' ' + str((int(a[2]))+4))
		neg.write('\n')


posstarts = open(bed.rstrip('.bed')+'.posstarts.bed')
dpos = {}
for line in posstarts:
        newline = line.rstrip()
	if newline in dpos:
		dpos[newline] += 1
	else:
		dpos[newline] = 1

negstarts = open(bed.rstrip('.bed')+'.negstarts.bed')
dneg = {}
for line in negstarts:
        newline = line.rstrip()
        if newline in dneg:
                dneg[newline] += 1
        else:  
                dneg[newline] = 1


import simplejson

with open(bed.rstrip('.bed')+'.neg.json','w') as f:
	simplejson.dump(dneg,f)

with open(bed.rstrip('.bed')+'.pos.json','w') as f:
	simplejson.dump(dpos,f)

