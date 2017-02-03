seen_lines = set() 
outputfile = open("unique_links.txt", "w")
for line in open("links.txt", "r"):
    if line not in seen_lines:
        outputfile.write(line)
        seen_lines.add(line)
outputfile.close()
