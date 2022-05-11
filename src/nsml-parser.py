import sys

args = sys.argv

html_exceptions = [{"html": "<!DOCTYPE html>"}]

nsml_file_path = args[1]

file = open(nsml_file_path, "r")

document_tree = {}
bracket_balance = 0
tags = []
for line in file:
    
    if line.find("{") != -1:
        tag = line[:line.find("{")]
        html_tag = {"element": tag.replace(" ", ""), "self_closing": False, "children": []}

        if tag.find("/") != -1:
            html_tag = { "element": tag[:tag.find("/")].replace(" ", ""), "self_closing": True, "children": None}
            tags += [html_tag]
        else:
           tags += [html_tag]   
   
print(tags)
