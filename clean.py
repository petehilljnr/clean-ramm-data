import sys
import os

inputfile = sys.argv[1]
outputfile = sys.argv[2]
delimiter = sys.argv[3]
config = sys.argv[4]

print 'Input: ' + inputfile
print 'Output: ' + outputfile
print 'Delimiter: ' + delimiter
print 'Config File: ' + config

infile = open(inputfile, 'r')
outfile = open('temp_data_file.txt', 'w')

headers = infile.readline()

num_delim = headers.count(delimiter)

print 'Number of fields is ' + str(num_delim + 1)
outfile.write(headers)


data = list(infile)

errors = 0
suspects = 0
char_buffer = 0
line_num = 1

for line in data:
    char_buffer = char_buffer + line.count(delimiter)
    #print line.replace("\n", "")
    if char_buffer == num_delim:
        outfile.write(line)
        char_buffer = 0
        line_num = line_num + 1

    elif char_buffer > num_delim:
        print "Suspect data on line " + str(line_num) + ' of the output file'
        outfile.write(line)
        line_num = line_num + 1
        char_buffer = 0
        suspects = suspects + 1

    elif line.count(delimiter) < num_delim:
        print "Error on line " + str(line_num) + ' of the output file'
        outfile.write(line.replace("\n", ""))
        errors = errors + 1

    else:
        print 'something strange ...'

print "Number of errors: " + str(errors)
print "Number of suspects: " + str(suspects)

infile.close()
outfile.close()

infile = open('temp_data_file.txt', 'r')
outfile = open(outputfile, 'w')
config = open(config, 'r')

header_order = list(config)
fields = []

config.close()

for field in header_order:
    fields.append(field.replace("\n", ""))

new_header = delimiter.join(fields)

outfile.write(new_header + "\n")
headers = infile.readline()
header_list = headers.replace("\n", "").split(delimiter)

for line in infile:
    values = line.replace("\n", "").split(delimiter)
    d = dict(zip(header_list, values))

    new_line = []

    for field in fields:
        if field in d:
            new_line.append(d[field])
        else:
            new_line.append('')

    out_line = delimiter.join(new_line)
    out_line = out_line + '\n'

    outfile.write(out_line)

outfile.close()
infile.close()
os.remove('temp_data_file.txt')
