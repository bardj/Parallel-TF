#To run:  python makematrix.py FILENAME MOTIFCENTERS.BED

import simplejson
import sys
import os
input = sys.argv[1]



from numpy import *
set_printoptions(threshold=nan,linewidth = nan)

#Loads json files into dictionary
dpos = simplejson.load(open(input+'.pos.json'))
dneg = simplejson.load(open(input+'.neg.json'))

#Loads motif centers
centers = open(sys.argv[2])


#Creates array of motif center sites
cents = []
for line in centers:
	line = line.rstrip()
	if 'r10' in line or 'r11' in line or 'r12' in line or 'r13' in line or 'r14' in line or 'r15' in line or 'r16' in line or 'r17' in line or 'r18' in line or 'r19' in line or 'r20' in line or 'r21' in line or 'r22' in line:
		for i in range(2):
			if i == 0:
				for b in range(-105,106):
					cents.append(line[:6]+str(int(line[6:])+b))
			else:
				for b in range(-105,106):
					cents.append(line[:6]+str(int(line[6:])-b))
	else:
		for i in range(2):
			if i == 0:
				for b in range(-105,106):
					cents.append(line[:5]+str(int(line[5:])+b))
			
			else:
				for b in range(-105,106):
					cents.append(line[:5]+str(int(line[5:])-b))

#Makes empty matrix
matrix = zeros((len(cents)/422,422))

#Makes a matrix where each row is a center and each column is base pair -105 to +105 from the center.  The values in the columns are the number of start values at the base pair.
for n in range(len(cents)):
	if n%422<211:
		if cents[n] in dpos:
                        matrix[n/422,n%422] = dpos[cents[n]]
	else:
		if cents[n] in dneg:
                	matrix[n/422,n%422] = dneg[cents[n]]

#Prints Matrix in format suitable for centipede
print '\n'.join(','.join(str(cell) for cell in row) for row in matrix)
