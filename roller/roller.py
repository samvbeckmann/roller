import sys
import re

# Main file for linter.
line_num = 0
file_line = ""
with open(sys.argv[1], 'r') as lintee:
    for file_line in lintee:
        line_num += 1
        if re.match("\s*$", file_line):
            continue
        if re.search("[ \t]$", file_line):
            print("%d. Statement should not have trailing whitespace." % line_num)

        if not re.match(".+[\{\};][\s]*$", file_line):
            print("%d. Statement should end with a semicolon." % line_num)

        if re.match("\s*\{\s*", file_line):
            print("%d. Open curly brace should not stand-alone." % line_num)
        if re.search("\{.*\}", file_line):
            print("%d. Closing curly brace should stand-alone." % line_num)

        if re.search("(?<!=)==(?!=)", file_line):
            print("%d. Should only use strict equality." % line_num)

        regex = re.search("(\".*\")", file_line)
        if regex is not None and not re.search("'", regex.string[regex.start():regex.end()]):
            print("%d. Should use single quotes." % line_num)

        if re.search(";.*;", file_line):
            print("%d. Use only one statement per line." % line_num)
        if len(file_line) > 80:
            print("%d. Lines should not be longer than 80 characters." % line_num)

    if not re.match(".*\n$", file_line):
        print("%d. File %s should end with a newline character." % (line_num, sys.argv[1]))
