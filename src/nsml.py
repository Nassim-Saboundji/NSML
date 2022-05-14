import sys

args = sys.argv

doctype = "<!DOCTYPE html>"

nsml_file_path = args[1]

file = open(nsml_file_path, "r")

elements = []
previous_element = ""
current_element = ""
content = ""
contents = []
brackets = ""
for line in file:
    open_curly_b = line.find("{")
    closed_curly_b = line.find("}")
    open_bracket = line.find("[")
    closed_bracket = line.find("]")

    if open_bracket != -1:
       tag_name = line[:open_bracket].replace(" ", "")
       attributes = line[open_bracket + 1: closed_bracket].replace(" ", "")
       if tag_name == "":
           tag_name = previous_element
       else: 
          previous_element = tag_name

       if "/" in tag_name:
        element = "<" + tag_name[:tag_name.find("/")] + " " + attributes + "/>"
        elements.append(element)
        current_element = element
       else:
        element = "<" + tag_name + " " + attributes + ">"
        elements.append(element)
        current_element = element
    
        

    if open_bracket == -1 and open_curly_b != -1:
        tag_name = line[:open_curly_b].replace(" ", "")

        if tag_name == "":
            tag_name = previous_element
        else: 
            previous_element = tag_name

        element = "<" + tag_name + ">"
        elements.append(element)
        current_element = element
        
    
    if open_curly_b == -1 and closed_curly_b == -1 and open_bracket == -1 and closed_bracket == -1:
        content += line
    
    if open_curly_b != -1:
        brackets += "{"

    if closed_curly_b != -1:
        contents.append({"element": current_element, "content": content})
        content = ""
        brackets += "}"



final_elements = []
for i, el in enumerate(contents):
    if el["content"] != "" and el["content"] != "\n":
        final_elements.append(el)



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

#print(final_hierarchy)

## This part allows use to get the correct DOM structure  
right_side = []
left_side = []
for i, position in enumerate(final_hierarchy):
    if position == "p":
        right_side.append(elements[i])
        left_side.append("</" + elements[i][elements[i].find("<") + 1: elements[i].find(" ")] + ">")
    if position == "c":
        tag = elements[i]
        right_side.append(elements[i])
        if "/" not in elements[i]:
            right_side.append("</"+ elements[i][elements[i].find("<") + 1: elements[i].find(" ")] + ">")


DOM_structure = right_side + list(reversed(left_side))
##

for el in DOM_structure:
    print(el)

for el in final_elements:
    print(el)


content_counter = 0
final_DOM = []
for tag in DOM_structure:
    final_DOM.append(tag)

    if content_counter > len(final_elements) - 1:
        continue

    if tag == final_elements[content_counter]['element']:
        final_DOM.append(final_elements[content_counter]['content'])
        content_counter += 1

for el in final_DOM:
    print(el)