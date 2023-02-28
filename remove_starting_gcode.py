#!/usr/bin/python3
import sys
import re
import os

sourceFile=sys.argv[1]

# // The commands that we want to eliminate
ext = re.compile("^M104")
ext2 = re.compile("^M109")
bed = re.compile("^M190")

# Track if the items has been found
foundEx = False
foundEx2 = False
foundBed = False

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()
    f.close()

#set the destination to the source file
destFile = sourceFile

with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
         oline = lines[lIndex];
         parts = oline.split(';', 1)
         if len(parts) > 0:
             command = parts[0].strip()
         if command:
            if not foundEx and re.search(ext, command) is not None:
                foundEx = True
            elif not foundEx2 and re.search(ext2, command) is not None:
                foundEx2 = True
            elif not foundBed and re.search(bed, command) is not None:
                foundBed = True
            else:
                of.write(command + "\n")
         else:
             of.write(oline)

    #Clean up
    of.close
