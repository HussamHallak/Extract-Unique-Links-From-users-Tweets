import sys
import urllib2
import json
if len(sys.argv) != 3:
        print "Usage: Python download_timemaps.py <input_file> <output_file>"
        print "e.g: Python download_timemaps.py unique_links.txt timemap.json"
else:
        i = 0
        with open(sys.argv[1]) as fp:
            for line in fp:
                link =  "http://memgator.cs.odu.edu/timemap/json/" + line
                response = urllib2.urlopen(link)
                content = json.load(response)
                output_file_name = 'TimeMaps\' + sys.argv[2] + str(i)
                dir_path = os.path.join(self.TimeMaps) 
                os.makedirs(dir_path)                             # create directory [current_path]/feed/address
                fh_output = open(os.path.join(dir_path, output_file_name), 'wb')
                #fh_output = open(output_file_name, "w")
                fh_output.write(content)
                fh_output.close()
fh_input.close()
