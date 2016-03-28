import sys
import os
import collections


def check_field_value(check_type, check_value):
    #need to add in checks for other data types
    if check_type == "timestamp" and check_value != "":
        temp1 = check_value.replace("a.m.", "AM")
        temp2 = temp1.replace("p.m.", "PM")
        return temp2
    elif check_type == "text" and check_value != "":
        temp1 = check_value.replace('"', "'").replace("\\", "\\\\").replace("\r", "")
        return temp1
    elif check_type == "money":
        temp1 = check_value.replace('$', '').replace(",", "")
        return temp1
    else:
        return check_value


def clean_file(inputfile, outputfile, config, delimiter="|"):

        try:
            infile = open(inputfile, 'r')
            outfile = open('temp_data_file.txt', 'w')
            headers = infile.readline()
            num_delim = headers.count(delimiter)
            outfile.write(headers)

            data = list(infile)
            errors = 0
            suspects = 0
            char_buffer = 0
            line_num = 1

            for line in data:
                char_buffer = char_buffer + line.count(delimiter)

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
                    #print "Error on line " + str(line_num) + ' of the  output file'
                    outfile.write(line.replace("\n", "").replace("\r", ""))
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
            fields = collections.OrderedDict()

            config.close()

            for field in header_order:
                field_config = field.split("->")
                field_name = field_config[0]
                field_type = field_config[1].replace("\n", "")
                fields[field_name] = field_type

            #new_header = '|'.join(fields.keys())

            #outfile.write(new_header + "\n")
            headers = infile.readline()
            header_list = headers.replace("\n", "").split(delimiter)

            for line in infile:
                values = line.replace("\n", "").split(delimiter)
                d = dict(zip(header_list, values))

                new_line = []

                for field in fields:
                    if field in d:
                        field_value = d[field]
                        field_type = fields[field]
                        new_line.append(check_field_value(field_type, field_value))
                    else:
                        new_line.append('')

                out_line = '|'.join(new_line)
                out_line = out_line + '\n'

                outfile.write(out_line)

            outfile.close()
            infile.close()
            os.remove('temp_data_file.txt')

            return {'fatals':0,'errors':errors,'suspects':suspects}

        except:
            return {'fatals':1,'errors':1,'suspects':1}




