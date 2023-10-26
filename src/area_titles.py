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
    filename = dirname[1] + "area-titles.csv"
    for filename in dirname:
        open(filename)
        for line in filename:
            data = line.strip().split(',')
            if int(data[0]) % 1000 != 0 and data[0]:
                record = {
                    data[0]: data[1]
                }
            areadict.append(record)
        filename.close()
    return areadict
    pass
