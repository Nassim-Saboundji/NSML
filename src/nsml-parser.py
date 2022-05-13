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

#print(DOM_structure)

class Parser(HTMLParser):
  # method to append the start tag to the list start_tags.
  def handle_starttag(self, tag, attrs):
    global start_tags
    start_tags.append(tag)
    # method to append the end tag to the list end_tags.
  def handle_endtag(self, tag):
    global end_tags
    end_tags.append(tag)
  # method to append the data between the tags to the list all_data.
  def handle_data(self, data):
    global all_data
    all_data.append(data)
  # method to append the comment to the list comments.
  def handle_comment(self, data):
    global comments
    comments.append(data)
start_tags = []
end_tags = []
all_data = []
comments = []
# Creating an instance of our class.
html_parser = Parser()
html_parser.feed("".join(DOM_structure))
print(start_tags)
print(end_tags)
print(all_data)
print(comments)