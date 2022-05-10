import sys

args = sys.argv

html_exceptions = [{"html": "<!DOCTYPE html>"}]

nsml_file_path = args[1]

file = open(nsml_file_path, "r")

document_tree = {}
bracket_balance = 0
for line in file:
    bracket_balance += 1 if line.find("{") != -1 else 0
    bracket_balance += -1 if line.find("}") != -1 else 0
    print(line, bracket_balance)
