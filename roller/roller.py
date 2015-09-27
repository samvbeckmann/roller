import sys, re
line_num = 0
file_line = ""
with open(sys.argv[1], 'r') as lintee:
    for file_line in lintee:
        line_num += 1
        if re.match("\s*$", file_line): continue
        if re.match(".*[ \t]$", file_line): print("%d. Statement should not have trailing whitespace." % line_num)
        if not re.match(".+[\{\};][\s]*$", file_line): print("%d. Statement should end with a semicolon." % line_num)
    if not re.match(".*\n$", file_line): print("%d. File %s should end with a newline character." % (line_num, sys.argv[1]))
