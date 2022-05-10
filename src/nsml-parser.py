import sys

args = sys.argv

nsml_file_path = args[1]

file = open(nsml_file_path, "r")

file_by_line = []
for line in file:
    file_by_line += [line]


