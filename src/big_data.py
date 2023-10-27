#!/usr/bin/env python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

import sys
import time

from area_titles import area_titles_to_dict
from report import Report
from util import record_matches_fips, record_is_all_industries, record_is_software_industry


if len(sys.argv) < 1:
    print("Program was not called correctly, please make sure you are in the directory: cs1440-assn3/ and on your command line type the following command replacing 'Directory' with the directory leading to area-titles.csv:\n$ python src/big_data.py Directory")
    sys.exit()
print("Reading the databases...", file=sys.stderr)
before = time.time()
areas = area_titles_to_dict(sys.argv)
print("TODO: Fill in the report using information from 'sys.argv[1]/2022.annual.singlefile.csv'")  # DELETE ME

rpt = Report(year=2022)
filename = sys.argv[1] + "/2022.annual.singlefile.csv"
with open(filename, 'r') as file:
    for line in file:
        record = line.strip().strip('"').split(',')
        if record_matches_fips(record, areas):
            if record_is_all_industries(record):
                rpt.all.add_record(record, areas)
            if record_is_software_industry(record):
                rpt.soft.add_record(record, areas)      


after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)

print("TODO: did you delete all of the TODO messages?")  # DELETE ME
