# CS 1440 Assignment 3: Big Data Processing - Project Requirements

*   Write a Python program to summarize data from the Bureau of Labor Statistics' Quarterly Census of Employment and Wages for the most recent year.
*   Data is sourced from a pair of Comma Separated File (CSV) files.
    *   The national data file contains over 3.6 million records, but only a small fraction has usable data.
*   Apply lessons from the previous assignment for inspiration, but do not copy code directly.
*   Keep in mind that certain design decisions have already been established for this project, and your role is to complete it following the existing design, rather than starting from scratch.


## Definitions

*   **Field**: A piece of string data.
*   **Record**: A line of text containing multiple fields separated by commas `,`.
*   **FIPS area code**: A Federal Information Processing Standards code, which is a 5-character alphanumeric identifier, resembling a ZIP code. More details below.
*   **Predicate function**: In computer programming, a *predicate* is a function that answers a yes/no question. Predicates can take parameters but can only return either `True` or `False`.
*   **Accessor function**: In computer programming, an *accessor* is a function that returns a value from a collection or object.
*   **Test Driven Development (TDD)**: A programming approach where unit tests are written first, before writing the code to be tested.



## Test Driven Development

This assignment focuses on **Test Driven Development (TDD)**, which differs from your usual approach to homework. TDD requires more upfront study of the starter code and a better understanding of how the entire project fits together.

* Your task is to complete the program so that it passes all the provided unit tests.
    *   Do not alter the tests to force them to pass.
    *   Adjust the code to align with the tests, not the other way around.
    *   You are allowed, *but not required* to add more unit tests to the suite.
* Avoid changing the *function signatures* in the starter code; simply fill in the functions' bodies.
* After passing all unit tests, complete `big_data.py` to finalize the project.
    * For the final testing phase, use Unix text tools to generate datasets in `data/` for system tests.
    * Compare the program's output with the provided samples.
    * If all unit tests pass, the program's output should exactly match the samples.


### Running The Unit Tests

*   This project contains 23 unit tests.
*   At the end of the sprint all 23 tests must pass.
*   Do not edit the unit tests.
    *   If the tests do not pass, the problem is in the program, not the tests!

The unit tests may be run from the command line like this:

```bash
$ python src/run_tests.py
```

The code is structured into modules. It's recommended to tackle the modules in the following order:



## Utility Functions `util.py`

These essential functions are the heart of the program. They have concise bodies, typically one-liners, for easy testing and validation.  Creating functions for single lines of code is valuable because it allows for automated testing. When these fundamental building blocks are demonstrably correct, it instills confidence that the larger components of our program will function correctly as well.

**Predicates**:

0. `record_matches_fips(record, areas)`: Returns True if the record contains data about a FIPS area that belongs in the report.
1. `record_is_all_industries(record)`: Returns True if the record contains data about all industries in the economy, regardless of the ownership type.
2. `record_is_software_industry(record)`: Returns True if the record contains data about privately owned software publishing businesses.

**Accessors**:

3. `get_fips(record)`: Extract a FIPS area code from a record.
4. `get_estabs(record)` Extract the annual average of quarterly establishment counts from a record.
5. `get_emplvl(record)`: Extract the Annual average of monthly employment levels from a record.
6. `get_wages(record)`: Extract the sum of the four quarterly total wage levels from a record.



## Mapping FIPS Area Codes To Their Associated Area Titles `area_titles.py`

FIPS Area Codes play a central role in this program, serving two primary purposes:

0.  Identifying relevant records for the report: Since only a tiny fraction (0.05%) of the national file contributes data to the report, the FIPS area code serves as a key criterion to filter out irrelevant information.
1.  Providing human-friendly place names on the report: FIPS Area Codes also serve as a means to display easily understandable place names in the report.

Based on these requirements, it has been determined that using a dictionary is the most suitable data structure to fulfill both of these needs effectively.


### `area_titles_to_dict(dirname)`

This function takes a CSV file, `area-titles.csv`, located in a specified directory, and transforms it into a dictionary. The CSV file contains two columns: `area_fips` and `area_title`. In the resulting dictionary, FIPS area codes serve as keys, while their corresponding values are the user-friendly area titles. Further details about FIPS codes are provided below.

#### Parameter
*   `dirname`: String, the name of the directory where `area-titles.csv` is located.
    *   While the file name `area-titles.csv` is hard-coded into your program, the name of the directory containing it is specified by the user.
    *   You *may* add an extra front slash `/` between the `dirname` parameter and `area-titles.csv`.
    *   All information about this directory *must* be provided by the user; **do not** assume anything about the location of the file!
        *   The user is 100% responsible for specifying the directory name.
        *   Do not add extra strings such as `../`, `data/` to what the user enters on the command line.


#### Return Value
*    A dictionary where the keys are FIPS codes and the values are area titles.
*   The file `area-titles.csv` contains 4,726 lines of text, one of which the first is a CSV header line.
    *   After discarding unwanted data, the function returns a dictionary that contains **3,463** FIPS areas.


#### Implementation Details

This description is far longer than the function itself.  You can write this function in about 14 lines of code.  Don't overthink it!

0.  Initialize an empty dictionary
1.  Open the file `area-titles.csv` from the specified directory
    *   Your program does not modify `area-titles.csv`; neither should you edit it
    *   Just use this file as-is
2.  Discard the first line of `area-titles.csv` (the CSV header)
3.  Iterate through each line
    *   Split each line into **two fields**
        *   Read the `help()` documentation for `str.split` to learn how to split each line of this file into *exactly* two fields regardless of the number of commas it contains.
    *   Decide whether or not to include this FIPS area in the final report by looking at the **FIPS area code** in the first field
    *   The report *must* include data from all 50 states, the District of Columbia, and territories of the United States of America.
        *   This includes:
            *   The District of Columbia
            *   Puerto Rico
            *   Virgin Islands
            *   "Overseas Locations"
            *   "Multicounty, Not Statewide"
            *   "Out-of-State"
            *   and "Unknown Or Undefined" areas
        *   All of these are *easily* identified by looking only at their FIPS codes
    *   Exclude these areas:
        *   "U.S. combined" and "TOTAL" FIPS areas
        *   All areas labeled "statewide"
        *   MicroSAs
        *   MSAs
        *   CSAs
        *   Federal Bureau of Investigation – undesignated
    *   Including these FIPS areas makes your report double- and triple-count areas
        *   *Again, all of these can easily be identified by looking at their FIPS codes*
    *   Your program can make this determination *solely* from the `area_fips` field; do not consider the `area_title` field
    *   The report considers data only from counties and county-equivalent divisions
        *   For example, Louisiana has *parishes*, Alaska has *boroughs* and *census areas*, and Puerto Rico has *municipios*
4.  If the conditions are met, add the FIPS code and corresponding area title to the `areas` dictionary.
5.  Ensure that the file `area-titles.csv` is closed before exiting.
6.  Return the `areas` dictionary.


#### What Are FIPS Area Codes?

FIPS area codes uniquely identify geographic areas within the United States.  The area designated by a FIPS area code is much larger than a ZIP code, and one location may be represented by many overlapping FIPS areas.  There are even FIPS codes which represent the nation as a whole.  It is important for the accuracy of the report that overlapping areas are excluded so as to not double-count statistics.

The format of FIPS area codes are described in [QCEW Area Codes and Titles](https://data.bls.gov/cew/doc/titles/area/area_guide.htm).  Part of the assignment is to read and thoroughly understand this document.


#### FIPS Codes Hints

*   FIPS area codes follow a *simple pattern* which make it easy to exclude unwanted areas
*   If your program inspects the human-friendly area title, you're doing it wrong
*   While some FIPS area codes look like integers, *never* convert them to numbers


## The IndustryData Class `industry_data.py`

This class contains statistics for a single industry.

*   Attributes
    *   `num_areas`: Integer, stores the number of areas in this part of the report.
    *   `total_annual_wages`: Integer, stores the total annual wages.
    *   `max_annual_wages`: List, stores the area (a string) with the maximum annual wage and its value (an integer). Format: `[area, wage]`
    *   `total_estabs`: Integer, stores the total number of establishments.
    *   `max_estabs`: List, stores the area (a string) with the maximum number of establishments and its value (an integer). Format: `[area, num]`
    *   `total_emplvl`: Integer, stores the total number of employees.
    *   `max_emplvl`: List, stores the area (a string) with the maximum number of employees and its value (an integer). Format: `[area, num]`
*   The initializer `__init__(self)` doesn't require any parameters.
    *   This is because the object is designed to accumulate data incrementally over time.
    *   Since the final values aren't known when the object is created, there's no need to pass any initial values to the constructor.
    *   Just ensure that the attributes are initialized with these default values.
        *   Integers are initialized to `0`
        *   Strings are initialized to `""`
*   Method
    *   `add_record(self, record, areas)`
        *   Adds a record's data to the summary statistics.
        *   This method does not need to validate its input; the record must be validated before this method is called.
        *   Parameters:
            *   record: A record containing employment and wage data.
            *   areas: A dictionary mapping FIPS area codes to human-friendly area titles.
        *   This method updates the following summary statistics:
            *   Adds one to the total number of areas processed.
            *   Calculates and accumulates the total annual wages.
            *   Keeps track of the area with the maximum annual wages.
            *   Calculates and accumulates the total number of establishments.
            *   Keeps track of the area with the maximum number of establishments.
            *   Calculates and accumulates the total employment level.
            *   Keeps track of the area with the maximum employment level.


## The Report Class `report.py`

**Do not edit this file!!!** If there is something wrong with the appearance of your report, the problem lies elsewhere.

Objects of this class collect statistics across two sectors of the economy.  It includes a `__str__` method to present this information as a printable report.

*   The initializer `__init__(self, year)` creates a `Report` object with a specified year (default is 1999).
    *   It also initializes the `all` and `soft` attributes as instances of `IndustryData`.
    *   At the beginning the two `IndustryData` objects contain zeroes and empty strings, and are filled in as the program encounters more data.
*   Attributes
    *   `year`: Integer, stores the year for the report. Default value is 1999.
    *   `all`: Instance of `IndustryData`, stores statistics for all industries in the economy.
    *   `soft`: Instance of `IndustryData`, stores statistics about privately held software publishing companies.
*   Methods
    *   `__str__()`: This method is provided for you, and creates a uniform string representation of the `Report` object when printed.
    *   `__repr__()`: This method is also provided for you, and just calls `__str__()`


### Processing `2022.annual.singlefile.csv`

As with the file `area-titles.csv`, the file name `2022.annual.singlefile.csv` shall be hard-coded into your program.  The name of the directory in which this file is found is supplied by the user on the command line.

Each line of this file is called a *record*.  Each record holds employment information about a single FIPS area, such as total wages paid, the number of people employed and the number of establishments for the year 2022.  

Every FIPS area is described by many records which cover various sectors of the economy.  Some records cover general economic data, while others delve into specific niches.  Moreover, as described above, some of the FIPS areas overlap.  The result is that the same economic data is counted in multiple records.  It is important to carefully select which records that are included in the final report, or else the report will double- or triple- count information!

The layout of this CSV file is described by [QCEW Field Layouts](https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm).  _Hint: you are using the **singlefile**_.

The fields in this file that are significant for our report are:

*   `area_fips`
*   `own_code`
*   `industry_code`
*   `year`
*   `total_annual_wages`
*   `annual_avg_emplvl`
*   `annual_avg_estabs`


#### How To Read `2022.annual.singlefile.csv`

*   Only one record from this file should be stored in memory at once
    *   Don't slurp the entire file into a variable as one giant string or as an array
        *   To be crystal clear: don't use `.read()` or `.readlines()`
        *   You may make temporary copies of the *current* record
        *   After you are done with the current record, you don't need to refer to it again
*   Your program will skip over the vast majority of records from this file in its search for the data our customer wants
    *   In addition to skipping records about excluded FIPS areas, your program will also skip records that don't belong to the sectors of the economy our customer is interested in
*   Numeric data must be converted from a string through an appropriate function
    *   `eval()` is **not** an appropriate function


#### Excluded FIPS areas

Some records contain data for areas that do not belong in the report.   Identify which records your program should skip over by inspecting the `area_fips` column.  See the section above titled *How to use the information from `area-titles.csv`*.


#### All Industries

Records pertaining to "all industries" include a reportable FIPS area, the `industry_code` field is `"10"`, and the `own_code` field is equal to `"0"`.


#### Software Publishing Industry

Records pertaining to the "software publishing industry" include a reportable FIPS area, the `industry_code` field is `"513210"` and the `own_code` field is equal to `"5"`.

**No other industry codes or ownership codes have a place in the report.**


## Command Line Interface

*   Unlike the previous assignment, this program takes exactly one argument, the name of a *directory*, not a *file*.
*   This program is an exception to our general rule about hard-coding file names into programs.
    *   For this assignment you *must* hard-code the names of the input files `area-titles.csv` and `2022.annual.singlefile.csv` into your program.
    *   Do not hard-code the directories containing these files.
    *   Do not code any assumptions about the program's current directory.  The program must work when run from *any* directory.
*   Do not read too much into the naming convention used by the data directories.
    *   The name of the directory containing this file **does not matter** to your program
    *   Your program must be able to work with *any* directory name that can be supplied on the command line, even directories not included with the starter code.
    *   For example, if `2022.annual.singlefile.csv` contains data only about Idaho but is in a directory named `"South_Dakota"`, your program will still print a report about Idaho.

To compute statistics for the entire economy of Washington D.C., from the repository's top directory run:

```
$ python src/big_data.py data/DC_complete
```

To generate the report against the national database, use this command:

```
$ python src/big_data.py data/USA_full
```

The user may or may not write a trailing slash `/` in the path they provide.  Your program must accept both kinds of paths.  For example, these two commands should both work:

```
$ python src/big_data.py data/USA_full
$ python src/big_data.py data/USA_full/
```

This is an easy requirement to meet.  You do not need to check whether the argument ends with `/`; always put a `/` between the command-line argument and the name of the file to open.  To your computer, both of these paths are equal:

*   `data/USA_full/area-titles.csv`
*   `data/USA_full//area-titles.csv`


Exactly one argument is required.  When too few or too many arguments are given, a message is printed and the program exits:

```
$ python src/big_data.py
Usage: src/big_data.py DATA_DIRECTORY


$ python src/big_data.py data/USA_full extra arguments
Usage: src/big_data.py DATA_DIRECTORY
```

When the specified directory is non-existent or inaccessible, let Python's `open()` function fail:

```
$ python src/big_data.py data/DERP
Traceback (most recent call last):
  File "src/big_data.py", line 220, in <module>
    fips = get_fips_areas(sys.argv[1])
  File "src/big_data.py", line 9, in get_fips_areas
    with open(f'{datadir}/area-titles.csv') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/DERP/area-titles.csv'
```


## System Testing

This repository contains sample input directories under `data/`, each of which contains three files:

*   `README.md`
    *   Instructions for trimming the full data set down using command line text tools
*   `area-titles.csv`
    *   The database of FIPS area codes
*   `output.txt`
    *   The correct output for this data set

This program's output must *exactly match* the examples down to the smallest detail.

*   The only output that should appear on STDOUT is produced by `print(rpt)`
    *   Your final submission *must not* print any other data to `sys.stdout`.
    *   Delete all of the `print()`s that output **TODO** messages
    *   You may keep calls to `print()` that write to STDERR
*   Clean up the text read from the CSV files so your program's output *exactly matches* the provided examples.  Your report should contain:
    *   no extra newlines
    *   no extra spaces
    *   no extra quote marks
    *   no FIPS codes; these must be shown as "County, State"
*   Check that your program finds the correct answers by redirecting its STDOUT to a file, and comparing to the examples with the `diff` tool:
    *   ```bash
        $ python src/big_data.py data/UT_all_industries > ut.txt
        $ diff -u --color=always ut.txt data/UT_all_industries/output.txt
        ```
    *   The `diff` text tool shows differences between two files
        *   When its arguments are identical, `diff` produces **no output**.  Pay close attention when it does print something!
        *   The options `-u --color=always` cause the output look like a Git diff.
    *   **Windows users** may find that *every* line of their program's output differs from the `output.txt` files that I provided, even though there are no apparant differences.   If this happens to you, add the `-Z` option to your command:
    *   ```bash
        $ python src/big_data.py data/UT_all_industries > ut.txt
        $ diff -u -Z --color=always ut.txt data/UT_all_industries/output.txt
        ```
        *   `-Z` tells `diff` to ignore the *end of line* (eol) characters in its input files; eol characters differ between Linux and Windows.
        *   Mac users shouldn't run into this issue
*   `diff` is how we will grade your submission, so you should make this part of your testing procedure!


### Hints For Filling In The Report

*   Study the starter code to learn how to use the report dictionary.
    *   Avoid creating extra variables; use the `rpt` object to store all data.
    *   Some fields within `rpt` hold integers, while others hold lists.
*   This program shares no code with the Text Tools you wrote last time.
    *   Borrow from the lessons you learned in the last assignment, not the code itself.


## Can I Use The Text Tools From The Previous Assignment?

Yes and no.

*   *You will* use the techniques you learned in that project on this assignment.
*   *You may* use your Text Tools to prepare small data sets for testing.
    *   See [Installing Your Text Tools](./Installing_Text_Tools.md) for details on how to do this.
    *   You are not expected to spend more than a few minutes installing your text tools.
    *   If you get stuck, just use the shell's built-in tools.
*   *Do not* copy code from the last program into this assignment.
    *   The problem you are solving this time is not close enough to the last project for this to be helpful.
    *   Students who try this end up creating extra trouble for themselves.
*   This program cannot run other programs to collect its results.
    *   The Text Tools are an external program.
    *   Do not use `os.system()`, `subprocess`, `pipes` or similar features to gather data.


## Make It Work Before You Make It Fast

The biggest CSV file under `data/USA_full` is quite large, and your program will need time to process it.

*   Don't even think about making your program faster until it consistently gives *correct answers*.
*   This program should finish in a *reasonable* amount of time
    *   You won't get a better grade if your program is *extra fast*
    *   You will lose points if your program is *too slow*
*   Because everybody's computer is different, one time limit is not fair
    *   Instead, use the [Performance Benchmark Tool](../demo/README.md) to see what a *reasonable* amount of time means for your computer
    *   If your program is slower than what the benchmark suggests, you are doing something wrong!

### Efficiency Tips

*   Minimize the number of times your program reads each file.  One pass per file is enough.
*   Minimize the number of `for` loops that are nested within other loops.
    *   This program does not require *any* nested `for` loops.
*   Do not read a file into an array and *then* loop through the array.
    *   Simply loop through the lines of the file, one at a time.
    *   You only need to look at records from the big data file once
*   Do not use a list or tuple to associate FIPS area codes with human-readable area titles.
    *   Use a dictionary.

> Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered.  We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.  Yet we should not pass up our opportunities in that critical 3%.
>
> – Donald Knuth
> "Structured Programming With Go To Statements"
> Computing Surveys, Vol 6, No 4, December 1974


## Can I use Python's `csv` module?

No.

*   For this assignment, `csv` provides no essential capabilities over the `str` class.
*   More importantly, the point of this assignment is to teach you how to process data *generally*.
    *   The `csv` module won't teach you how to solve problems when your data comes in a different format than CSV.
*   Put another way, CSV is a subset of plain text data.
    *   If you know how to deal with plain text you can deal with CSV, but the converse isn't necessarily true.
    *   You limit yourself if you can only solve problems when a module exists.

![](./consoomer.jpg "One of the programmers who will lose his job to Chat GPT this year")

Don't be a mere consumer; you can be the programmer who *makes* modules. _(Don't even ask about using `numpy` or `pandas`.  This assignment isn't that complicated.)_
