import sys
import urllib2
import json
from datetime import *

current_datetime = datetime.now()

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d0 - d1
print delta.days

if len(sys.argv) != 3:
    print "Usage: Python downloadcreationdatejson.py <input_file> <output_file>"
    print "e.g: Python downloadcreationdatejson.py unique_links.txt creation.json"
else:
    i = 0
    fh_input = open(sys.argv[1], 'r')
    fh_output = open(sys.argv[2], 'w')
    for line in fh_input:
        try:
            link =  "http://cd.cs.odu.edu/cd?url=" + line
            response = urllib2.urlopen(link)
            data = json.load(response)
            creation_date = data['Estimated Creation Date']
            creation_date_clean = creation_date[0:9]
            year_C = creation_date_clean.split('-')[0]
            month_C = creation_date_clean.split('-')[1]
            day_C = creation_date_clean.split('-')[2]
            month_C = month_C.lstrip("0")
            day_C = day_C.lstrip("0")
            date1 = date(year_C, month_C, day_C)
            today = date(current_datetime.year, current_datetime.month, current_datetime.day)
            old_in_days = (today - date1).days
            fh_output.write(old_in_days)
            fh_output.write("\n")
        except:
            print "This link came with an error code:"
            print "http://cd.cs.odu.edu/cd?url=" + line
    fh_input.close()
    fh_output.close()
