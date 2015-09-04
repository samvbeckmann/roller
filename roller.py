import sys

__author__ = 'SAM'


def has_valid_semicolon(line):
    """This checks a passed line to ensure it has proper semicolon usage"""
    if '{' in line or '}' in line:
        return True
    else:
        return line.endswith(';')


linenum = 0
with open(sys.argv[1], 'r') as myfile:
    for file_line in myfile:
        linenum += 1
        file_line = file_line.rstrip()
        if not file_line:
            continue
        if not has_valid_semicolon(file_line):
            print "%d. Statement should end with a semicolon" % linenum
