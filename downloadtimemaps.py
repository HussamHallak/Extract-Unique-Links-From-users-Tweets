import sys
import os
import urllib2
if len(sys.argv) != 3:
        print "Usage: Python download_timemaps.py <input_file> <output_file>"
        print "e.g: Python download_timemaps.py unique_links.txt timemap.txt"
else:
        fh_input = open(sys.argv[1], 'r')
        i = 0
        with open(sys.argv[1]) as fp:
            for line in fp:
                link =  "http://memgator.cs.odu.edu/timemap/link/" + line
                print link
                try:
                        response = urllib2.urlopen(link)
                        content = response.read()
                        output_file_name = sys.argv[2] + str(i)
                        fh_output = open(output_file_name, "w")
                        fh_output.write(content)
                        fh_output.close()
                except:
                        print "error"
        fh_input.close()

