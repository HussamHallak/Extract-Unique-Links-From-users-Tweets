import sys

if len(sys.argv) != 3:
  print "Usage: Python parse_timemap.py <input_file> <output_file>"
  print "e.g: Python parse_timemap.py time_map.txt report.txt"
else:
  i = 0
  fh_output = open(sys.argv[2] , 'w')
  for counter in range(1,1000):
    input_file_name = sys.argv[1] + str(i)
    fh_input = open(input_file_name,'r')
    i = i + 1
    number_of_mementos = 0;
    while text = fh_input.readline():
      if 'datetime' in text:
        number_of_mementos = number_of_mementos + 1
    fh_output.write(number_of_mementos)
    fh_output.write('\n')
  fh_input.close()
  fh_output.close()
