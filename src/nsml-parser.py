import enum
import sys

args = sys.argv

doctype = "<!DOCTYPE html>"

nsml_file_path = args[1]

file = open(nsml_file_path, "r")

document_tree = {}
bracket_balance = 0


tags = []
brackets = []
for i, line in enumerate(file):
    
    if line.find("{") != -1:
        tag = line[:line.find("{")].replace(" ", "")
        brackets += "{"
        
        tags.append(tag)

    if line.find("}") != -1:
        brackets += "}"


for i, tag in enumerate(tags):
    if tag == "":
        tags[i] = tags[i-1]


print(brackets)
print(tags)


hierarchy = "".join(brackets)
hierarchy = hierarchy.replace("{}", "c")

nb_brackets = 0
for c in hierarchy:
    if c == "}" or c == "{":
        nb_brackets += 1

print(nb_brackets)
print(hierarchy)

final_hierarchy = []
for c in hierarchy:

    if c == "}":
        continue

    if c == "{":
        final_hierarchy.append("p")
    
    if c == "c":
        final_hierarchy.append("c")
    

print(final_hierarchy)

