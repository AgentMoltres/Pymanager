#!/usr/bin/env python

import os, sys
from os.path import exists
print "Python file manager"
loc = raw_input("File location sir >")
print loc
def main():
    try:
        loc_real = open(loc)
    except:
        print "File location isn't there!"   
    input = raw_input("Remove/Write/Read/CHByte/Quit:").lower()
    if input == "remove":
        os.remove(loc)
        main()
    elif input == "write":
        loc_real.write(raw_input("Input what you want to write: "))
        main()
    elif input == "read":
        file_con = loc_real.read()
        print file_con
        main()
    elif input == "chbyte":
        print "Size is %d" % len(loc)
        main()
    elif input == "quit" or "q":
        print "Bye"
        sys.exit(1)
main()
