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


if sys.argv is None:
    print("Program was not called correctly, please make sure you are in the directory: cs1440-assn3/ and on your command line type the following command replacing 'Directory' with the directory leading to area-titles.csv:\n$ python src/big_data.py Directory")
    sys.exit()
print("Reading the databases...", file=sys.stderr)
before = time.time()
areas = area_titles_to_dict(sys.argv)

print("TODO: Fill in the report using information from 'sys.argv[1]/2022.annual.singlefile.csv'")  # DELETE ME

rpt = Report()
rpt.all.num_areas           = 1337
rpt.all.total_annual_wages  = 13333337
rpt.all.max_annual_wages    = ["Trantor", 123456]
rpt.all.total_estabs        = 42
rpt.all.max_estabs          = ["Terminus", 12]
rpt.all.total_emplvl        = 987654
rpt.all.max_emplvl          = ["Anacreon", 654]
rpt.soft.num_areas          = 1010
rpt.soft.total_annual_wages = 101001110111
rpt.soft.max_annual_wages   = ["Helicon", 110010001]
rpt.soft.total_estabs       = 1110111
rpt.soft.max_estabs         = ["Solaria", 11000]
rpt.soft.total_emplvl       = 100010011
rpt.soft.max_emplvl         = ["Gaia", 10110010]


after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)

print("TODO: did you delete all of the TODO messages?")  # DELETE ME
