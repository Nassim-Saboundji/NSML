import enum
import sys
from html.parser import HTMLParser

args = sys.argv

doctype = "<!DOCTYPE html>"

nsml_file_path = args[1]

file = open(nsml_file_path, "r")

document_tree = {}
bracket_balance = 0


tags = []
attributs = []
brackets = []
for i, line in enumerate(file):
    
    if line.find("{") != -1:
        tag = line[:line.find("{")].replace(" ", "")
        brackets += "{"
        
        tags.append(tag)

    if line.find("}") != -1:
        brackets += "}"

    if line.find("[") != -1 and line.find("]") != -1:
        attributs.append(line[line.find("[") + 1:line.find("]")])

for i, tag in enumerate(tags):
    if tag == "":
        tags[i] = tags[i-1]


hierarchy = "".join(brackets)
hierarchy = hierarchy.replace("{}", "c")

nb_brackets = 0
for c in hierarchy:
    if c == "}" or c == "{":
        nb_brackets += 1

final_hierarchy = []
for c in hierarchy:

    if c == "}":
        continue

    if c == "{":
        final_hierarchy.append("p")
    
    if c == "c":
        final_hierarchy.append("c")
    
right_side = []
left_side = []
for i, position in enumerate(final_hierarchy):
    if position == "p":
        right_side.append("<"+tags[i]+">")
        left_side.append("</"+tags[i]+">")
    if position == "c":
        right_side.append("<"+tags[i]+">")
        right_side.append("</"+tags[i]+">")


DOM_structure = right_side + list(reversed(left_side))

print(attributs)
print(DOM_structure)

