# CS 1440 Assignment 3: Big Data Processing

*   [Instructions](./instructions/README.md)
    *   [Running Unit Tests](./instructions/Running_Unit_Tests.md)
    *   [Test Data](./data/README.md) for system testing
    *   [Installing Your Text Tools](./instructions/Installing_Text_Tools.md)
    *   [How to Submit this Assignment](./instructions/How_To_Submit.md)
*   [Project Requirements](./instructions/Requirements.md)
*   [Performance Benchmark Tool](./demo/README.md)


*Note: this file is a placeholder for your notes.  When seeking help from TAs or tutors, replace this text with a description of your problem and push it to GitLab*


## Get the starter code

*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$` (that represents your shell's prompt).
    *   Replace `USERNAME` with your GitLab username, `LAST` and `FIRST` with your names as used on Canvas.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn3 cs1440-assn3
$ cd cs1440-assn3
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn3.git
$ git push -u origin --all
```


## Overview

Your last project was a great success! The customer was very pleased with their new Text Tools and so impressed with the quality of your work that they have decided to contract you to finish the entire project for them.

This program's task is to analyze a large body of data and produce a summary report.  This program analyzes national employment data collected by the U.S. Bureau of Labor Statistics in 2022.  The report consists of two sections, a summary across all industries and a summary across the software publishing industry.  I worked with the customer long enough to develop the format of the report and create unit tests.  It is up to you to finish the program and use it on a 490MB CSV file to generate the report.  The link to this file is in the main [instructions](./instructions/README.md).


## Performance

Your program should run in a reasonable amount of time.  Use the [Performance Benchmark Tool](./demo/README.md) to learn how fast your program should be.


## Running Unit Tests

The starter code consists of 23 test cases, of which only two succeed at the outset.  You will increase the number of passing tests as you progress.

*   You may run the unit tests through PyCharm or the shell.
*   The unit tests are files in the directory `src/tests`
*   To run the tests from your shell, first `cd src`, then run `python run_tests.py`.
*   Full instructions are found in [Running Unit Tests](./instructions/Running_Unit_Tests.md).


## Expected Output

Each subfolder of [./data/](data) contains a file named `output.txt`.  The output your program produces should match these examples **exactly**.

Instructions are provided for creating the testing data sets using standard Unix text tools.  You can even use the text tools you wrote in Assignment #2.  These crafted input files are an important part of your testing phase.
