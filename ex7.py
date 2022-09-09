# argument_parsing

# Create three applications in three files. Each of these is to parse arguments 
# given on the command line. 
# 
# 
# # app1.py
# =====

# The application in this file will read the command line options using `sys.argv`.

# If one of the options is `--help`, it should output a small help text.

# If one of the options is `--fast` is should print the text "fast mode enabled" to the command line.

# If `--fast` is not one of the options it should print the text "slow mode enabled" to the command line.

import sys

a = sys.argv[1]
x = ("--help")
y = ("--fast")
z = x or y

if z == ("--help"):
    print("sdffdhd\nhgjgjgfj\nfhhgh")
elif z == ("--fast"):
    print("fast mode enabled")
else:
    print("slow mode enabled")