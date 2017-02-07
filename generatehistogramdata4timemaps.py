import sys
from collections import Counter

if len(sys.argv) != 3:
    print "Usage: Python generatehistogramdata4timemaps.py <input_file> <output_file>"
    print "e.g: Python generatehistogramdata4timemaps.py timemaps_report.txt timemap_histogram_data.txt"
else:
    fh_output = open(sys.argv[2] , 'w')
    number_of_memes = []
    fh_input = open(sys.argv[1], "r")
    
    for line in fh_input:
        number_of_memes.append(line)
    
    C = Counter(number_of_memes)
    file_header = "Number of memes (X)                  Links count (Y)\n"
    fh_output.write(file_header)

    for k,v in C.items():
        data = str(k) + "                    " + str(v)
        fh_output.write(data)

    fh_input.close()
    fh_output.close()       
    
#N = [1,2,3,3,3,4,4,4,5,5,5]
#C = Counter(N)
#for k,v in C.items():
  #print str(k) + " " + str(v)
#print [ [k,]*v for k,v in C.items()]
