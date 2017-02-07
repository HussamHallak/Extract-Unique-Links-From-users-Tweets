import sys
import json

if len(sys.argv) != 3:
    print "Usage: Python parsejsontimemap.py <input_file> <output_file>"
    print "e.g: Python parsejsontimemap.py timemap.json timemap_report.txt"
else:
    fh_output = open(sys.argv[2] , 'w')
    i = 1
    for i in range(0,999):
        input_file_name = sys.argv[1] + str(i)
        if (fh_input = open(input_file_name, 'r')):
            data = json.loads(json_data)
            number_of_mementos = len(data['mementos'])
            i = i + 1
            fh_output.write(number_of_mementos)
            fh_output.write('\n')
            fh_input.close()
    fh_output.close()
