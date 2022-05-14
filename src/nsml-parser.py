import enum
import sys
from xml.etree.ElementTree import QName

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
        attributs.append({"element": tags[len(tags)-1] ,"attributs": line[line.find("[") + 1:line.find("]")]})

for i, tag in enumerate(tags):
    if tag == "":
        tags[i] = tags[i-1]

for i, attribut in enumerate(attributs):
    if attribut["element"] == "":
        attributs[i]["element"] = attributs[i-1]["element"]

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
        if tags[i].find("/") != -1:
            right_side.append("<"+tags[i]+">")
        else:
            right_side.append("<"+tags[i]+">")
            right_side.append("</"+tags[i]+">")


DOM_structure = right_side + list(reversed(left_side))

print(attributs)
print(DOM_structure)

attributs_index = 0
for i, element in enumerate(DOM_structure):
    
    if attributs_index > len(attributs) - 1:
        break
    
    if element.replace("<", "").replace(">", "").replace("/", "") == attributs[attributs_index]["element"]:
        if element.find("/>") != -1:
            DOM_structure[i] = element[:element.find("/>")] + " " + attributs[attributs_index]["attributs"] + "/>"
        else:
            DOM_structure[i] = element[:element.find(">")] + " " + attributs[attributs_index]["attributs"] + ">"
        
        attributs_index += 1

print(DOM_structure)