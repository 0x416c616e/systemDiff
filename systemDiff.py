#!/usr/bin/env python3

print("systemDiff")
#make a test checksum comparison of a single file in the current directory
#first run should be a "before" run
#because there is nothing to compare from a previous run
#all subsequent runs are "after" runs
#and after the "after" run is finished, it puts the differences in a log file with a timestamp
#and the after.log contents are put into the before.log file
#then the after.log file is cleared out (blank but still exists)

import sys
if (len(sys.argv) == 1):
    print("Error: program must be run with an argument")
else:
    if (sys.argv[1] == "--before"):
        #general 'before' scan of the entire system
        print("running a 'before' scan")
    elif (sys.argv[1] == "--after"):
        #general 'after' scan of the entire system
        print("running an 'after' scan")
    elif (sys.argv[1] == "--custom"):
        #custom scan, can be useful for apache htdocs monitoring, for example
        #involves a config file
        #outputs to custom.log
        print("running custom scan for specific checksums and specific files/dirs/processes")
