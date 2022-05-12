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
hierarchy = hierarchy.replace("{}", "C")

print(hierarchy)

