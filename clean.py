#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]
delimiter = sys.argv[3]

print 'Input: ' + inputfile
print 'Output: ' + outputfile
print 'Delimiter: ' + delimiter

infile = open(inputfile, 'r')
outfile = open(outputfile, 'w')

headers = infile.readline()

num_delim = headers.count(delimiter)

print 'Number of fields is ' + str(num_delim)
outfile.write(headers)

data = list(infile)

line_num = 1

for line in data:
    if line.count(delimiter) == num_delim:
        #correct number
        outfile.write(line)

    #elif line.count(delimiter) < num_delim:
        #not enough numbers
    #    print 'Error on line ' + str(line_num)
    #    thisline = infile.readline()
    #    print thisline

    line_num = line_num + 1

infile.closed
outfile.closed
