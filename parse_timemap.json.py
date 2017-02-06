import sys
import json

if len(sys.argv) != 3:
    print "Usage: Python parse_timemap.json.py <input_file> <output_file>"
    print "e.g: Python parse_timemap.py timemap.json report.txt"
else:
    i = 0
    fh_output = open(sys.argv[2] , 'w')
    for counter in range(0,999):
        input_file_name = sys.argv[1] + str(i)
        with open(input_file_name) as json_data:
        data = json.loads(json_data)
        number_of_mementos = len(data['mementos'])
        i = i + 1
        fh_output.write(number_of_mementos)
        fh_output.write('\n')
    fh_output.close()
    
    #with open('strings.json') as json_data:
    #d = json.load(json_data)
#data = json.loads(array)
#for element in data['drinks']:
#    print element
