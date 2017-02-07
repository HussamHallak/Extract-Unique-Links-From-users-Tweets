import sys
import urllib2
import json
if len(sys.argv) != 3:
    print "Usage: Python downloadtimemapsjson.py <input_file> <output_file>"
    print "e.g: Python downloadtimemapsjson.py unique_links.txt timemap.json"
else:
    i = 0
    fh_input = open(sys.argv[1])
    for line in fh_input:
        link =  "http://memgator.cs.odu.edu/timemap/json/" + line
        response = urllib2.urlopen(link)
        content = json.load(response)
        output_file_name = sys.argv[2] + str(i)
        fh_output = open(output_file_name, "w")
        json.dump(content, fh_output)
        #fh_output.write(content)
        fh_output.close()
    fh_input.close()
