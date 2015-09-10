# clean-ramm-data

This is my attempt to clean carriage returns and empty lines out of text data files specifically out of RAMM.
It uses the header line to determine the number of fields it should hold and outputs to a new text file

It counts the number of instances of the delimiter on each line.
It uses that, and a running count of that, to know when to trim the <strong>"\n" new line</strong> characters from the file.

### Current Usage:
<code> python clean.py inputfile.txt outputfile.txt "delimiter" </code>

### To Do:
1.  Wrap the arguments in into <strong> getopt </strong>
2.  Process entire directories instead of single files
3.  Re-order fields based on field names from a configuration file (to ensure consistent importing into a database)
