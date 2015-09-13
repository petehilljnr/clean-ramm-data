# clean-ramm-data

This is my attempt to clean carriage returns and empty lines out of text data files specifically out of RAMM.
It uses the header line to determine the number of fields it should hold and outputs to a new text file

It counts the number of instances of the delimiter on each line.
It uses that, and a running count of that, to know when to trim the <strong>"\n" new line</strong> characters from the file.

You can also supply a text file with the column headers in the correct order (new one on each line) and it will re-order your output file to match the order.  Column names must match, and empty column holders with the correct name will be created in their place if they do not match.

### Current Usage:
<code> python clean.py inputfile.txt outputfile.txt "delimiter" columnheaders.txt</code>

### To Do:
1.  Wrap the arguments in into <strong> getopt </strong>
2.  Process entire directories instead of single files

