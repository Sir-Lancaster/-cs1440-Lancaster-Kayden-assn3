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

def area_titles_to_dict(dirname):
    """
    This function locates a CSV file called `area-titles.csv` in
    the specified directory, and transforms it into a dictionary
    """
    areadict = {}
    filename = str(dirname[1].strip()) + "area-titles.csv"
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0].strip('"').isdigit() and not data[0].strip('"').endswith("000"):
                areadict[data[0].strip('"')] = data[1].strip('"')
    return areadict

    pass
