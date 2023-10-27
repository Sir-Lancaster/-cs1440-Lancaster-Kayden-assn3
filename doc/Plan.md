# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).
*   [ ] **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*

### My Analysis
* This program aims to take a large file from the Beuro of Labor Statistics and parse through the large CSV files to generate a report about the information contained therein. It is my job to write the functions that gather only the desired information on the desired FIPS locations.
    * **utility** functions that will determine whether a the information is the desired areas I am looking for, then whether it is the correct information I am looking for in said area.
    * **area_titles** will take the data from area_titles.csv and convert it to a dictionary.
    * **add_record** adds the data from the file to the report.
    * **big_data** is the main function that ties it all together. 
* All of the data in this program comes from two files: area_titles.csv and 2022.annual.singlefile.csv
    * The latter will be used to gather all of the information for the report.
    * The former will be used to generate a dictionary.
    * A good solution will iterate the the csv files as few times as possible, will run swiftly, and will not crash unless it is the fault of the user. 
    * **Knowns:**
        * How to parse a file.
        * How to use the unit functions.
        * How to initialize a dictionary.
    * **Unknowns:**
        * The main thing that comes to mind is how to get a function to creat and add elements to a dictionary from the csv file.
    * **unknown unknowns:**
        * anything that i find later. 


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*
I am not going to design big_data.py because it simply calls all of the other modules. If i am writing it later and am struggling I will delete this statement and design it.

### Util.py
The heart of the program.

#### record_matches_fips(record, area)
```python
   # Predicate that takes a QCEW record and dictionary of FIPS areas and decides whether the record contains information about a FIPS area in the dictionary
   # because the function signiture contains record and area it can be assumed that the function will not need to open the file.

   if record is in area
        return True
    else 
        return false
```
This function simply asks if the QCEW record that is passed to this function is in the area dictionary, in which case it will return true. If it is not in the dictionary it will return false and move on. 

#### record_is_all_industries(record)
```Python 
#    Predicate that takes a QCEW record and decides whether the record contains information about all industries under all types of ownership throughout the entire economy
    if record[2] == '10'
        return True
    else
        return False
```
Simply looks at the third field and returns true if the industry code is 10, meaning that it is all industries. 

#### record_is_software_industry(record)
```Python
#   Predicate that takes a QCEW record and decides whether the record contains information about privately owned software publishing firms
    if record[2] == '513210' and record[1] == '5'
        return True
    else 
        return False
```
Checks to see that both the industry code is 513210 and the own code is 5, then returns true. if one is not true then it will return false. 

#### get_fips(record)
```Python
#    Extracts a FIPS area code from a QCEW record
    return record[0]
```
FIPS codes are in the first field so the function will return what is in the first field. 

#### get_estabs(record)
```Python 
#   Extracts the annual average of quarterly establishment counts for a given year from a QCEW record
return record[13]
```
this will look at the annual average of quarterly establishment counts and will return it so that it can be used for the report. 

#### get_emplvl(records)
```Python
#    Extracts the annual average of monthly employment levels for a given year from a QCEW record
return record[14]
```
Same as the last one but returns emplvl

#### get_wages(record)
```Python
#    Extracts the sum of the four quarterly total wage levels for a given year from a QCEW record
return record[15]
```
returns the total anual wages. 

#### area_titles_to_dict(dirname)
```Python
#    This function locates a CSV file called `area-titles.csv` in the specified directory, and transforms it into a dictionary
areadict = []

for area-titles.csv in dirname
    open(area-titles.csv)
    for line in area-titles.csv
        if int(data[0]) % 1000 !== 0
            data = line.strip().split(',')
            record = {
                data[0]: data[1]
            }
        areadict.append(record)
    close(area-titles.csv)
    return areadict
```
October 24: this will open area-titles.csv and will read each line for the FIPS and the name of the area, format them temporarily in the record variable and then append the record variable to the dictionary. It will probably need some tweeking to get it to work propperly. 

October 25: Added the if statement that will filter out the bad FIPS. 

#### __init__(self)
```Python
        num_areas = 0
        total_anual_wages = 0
        max_annual_wages = ["", 0]
        
        total_estab = 0
        max_estab = ["", 0]

        total_empl = 0
        max_empl = ["", 0]
```
Initializes all of the attributes for the industry data class.

### add_reacord(self, record, areas)
```Python
for record[0] in areas
    num_areas += 1
    CurrentRecordFIPS = getFIPS(record)
    CurrentRecordWages = getwages(record)
    total_annual_wages += CurrentRecordWages
    if CurrentRecordWages > max_annual_wages[1]
        max_annual_wages = [areas[CurrentRecordFIPS], CurrentRecordWages]
    
    CurrentRecordEstab = getestabs(record)
    total_estab += CurrentRecordEstab
    if CurrentRecordEstab > max_estab[1]
        max_estab = [areas[CurrentRecordFIPS], CurrentRecordEstab]
    
    CurrentRecordEmplvl = getemplvl(record)
    total_empl += CurrentRecordEmplvl
    if CurrentRecordEmplvl > max_empl[1]
        max_empl = [areas[CurrentRecordFIPS], CurrentRecordEmplvl]
```
Each of these three "bodies" of code are identical in structure. First we define a variable for the current record xxxx (xxxx being the wages, establishments, and employee levels) and assign it a variable using the util get functions. Then we add the new variable to the total_xxxx attributes from the initializer. Finaly we compare the Current Record xxxx to the max_xxxx at index 1 (to avoid the error of comparing an int to a string), and reassign the new variable to the max atribute if necessary. 
**Important - do not change the code in this phase**


Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.
*   [ ] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.

I have finally finished phase 2. On all of my functions I had to add the .strip() statement. The code works right now, but it is going over WAY too many FIPS and so I will need to look into why thats happening. I can't think of anything else that was noteworthy. The main reason it took so long was just because I either had the wrong .strip() writen, or I made small syntax errors with them. Something weird has been happening with the run_tests.py though. On the area-titles.csv that it is supposed to be passing to the function, it is passing earea-titles.csv. gotta email a TA about that. 

## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.
### run_tests.py
* From the src/ directory in the command line type "python run_tests.py"
* To fix the utility functions I had to strip the record paramater of quote marks for them to pass. 
* IndustryData class was failing because I had forgotten to put self. before I tried to update the atributes. 
* area_titles_to_dict was failing because I had written the filename variable wrong, and it was simply a matter of rewriting it so that it was not dirname[1] and was just dirname. 
* add_record function of IndustryData was also failing for the same reason as area_titles_to_dict.
* add_record was failing because I had all of the function nested into a for loop so it was double counting the num_areas variable. Taking it out of the for loop fixed it. 

### Other tests
I have run all of these commands from the 'cs1440_assn3/' directory. 
#### DC tests

```bash
python src/big_data.py data/DC_all_industries > DC.txt
diff -u --color=always DC.txt data/DC_all_industries/output.txt
```

```bash
python src/big_data.py data/DC_complete > DC.txt
diff -u --color=always DC.txt data/DC_complete/output.txt
```

```bash
python src/big_data.py data/DC_software_industry > DC.txt
diff -u --color=always DC.txt data/DC_software_industry/output.txt
```
No errors occured after running these tests.
#### IN tests
```bash
python src/big_data.py data/IN_all_industries > IN.txt
diff -u --color=always IN.txt data/IN_all_industries/output.txt
```
**EVENT:**
 Total annual wages                   $180,739,411,695
-Area with maximum annual wages       Marion County                     difference detected
+Area with maximum annual wages       Marion County, Indiana            correct output
 Maximum reported wages               $42,766,021,296

 Total number of establishments       186,198
-Area with most establishments        Marion County                     Difference
+Area with most establishments        Marion County, Indiana
 Maximum # of establishments          27,058

 Total annual employment level        3,113,422
-Area with maximum employment         Marion County                     Difference
+Area with maximum employment         Marion County, Indiana
 Maximum reported employment level    607,919

**FIX:** 
Had to change line 29 in area_titles.py to be:
```python
data = line.strip().split('","')
```

```bash
python src/big_data.py data/IN_software_industry > IN.txt
diff -u --color=always IN.txt data/IN_software_industry/output.txt
```
#### NH+RI tests
```bash
python src/big_data.py data/NH+RI_complete > NH+RI.txt
diff -u --color=always NH+RI.txt data/NH+RI_complete/output.txt
```

```bash
python src/big_data.py data/NH+RI_reversed > NH+RI.txt
diff -u --color=always NH+RI.txt data/NH+RI_reversed/output.txt
```
#### USA_full test
```bash
python src/big_data.py data/USA_full > USA.txt
diff -u --color=always USA.txt data/USA_full/output.txt
```
#### UT tests
```bash
python src/big_data.py data/UT_complete > UT.txt
diff -u --color=always UT.txt data/UT_complete/output.txt
```

```bash
python src/big_data.py data/UT_reversed > UT.txt
diff -u --color=always UT.txt data/UT_reversed/output.txt
```
These tests should not produce any output other that if there is a problem. Any events were recorded.
After running these tests I ran the following command to remove the txt files:
```bash
rm DC.txt IN.txt NH+RI.txt USA.txt UT.txt
``` 
## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab.
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
