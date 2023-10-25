# CS 1440 Assignment 3: Big Data Processing - Running Unit Tests

The starter code consists of 23 test cases, 2 of which already pass.  You will increase the number of passing tests as you progress in the project.


## Running all test suites

*   You may run the unit tests through PyCharm or the shell.
*   To execute the tests from your shell, first `cd src` then run `python run_tests.py`.  This script is a convenient way to execute all of the tests in one go.  It produces a lot of output:

```
$ cd src
$ python run_tests.py
test_50_states (tests.test_area_titles.TestAreaTitles.test_50_states)
The areas dictionary contains FIPS codes representing all 50 states ... ERROR
test_dictionary_length (tests.test_area_titles.TestAreaTitles.test_dictionary_length)
The areas dictionary contains 3,463 pairs ... ERROR
test_keylen_is_5 (tests.test_area_titles.TestAreaTitles.test_keylen_is_5)
The areas dictionary contains no keys != len() of 5 ... ERROR

... dozens of lines snipped ...

FAIL: test_record_matches_fips (tests.test_util.TestUtil.test_record_matches_fips)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/fadein/school/Fa23/cs1440/Assn/3-Big_Data/starter/src/tests/test_util.py", line 37, in test_record_matches_fips
    self.assertTrue(record_matches_fips(self.all_good, self.areas))
AssertionError: None is not true

----------------------------------------------------------------------
Ran 23 tests in 0.005s

FAILED (failures=7, errors=14)
```

The interpretation of this output is explained below.


## Running a single test suite

You may also execute an individual unit test suite.  Do this when you are focusing on just one part of the project and don't want to wade through unnecessary output.

The command to run a single suite is different than `run_tests.py`.

1.  First, change into the `src/` directory 
2.  Then run this command, substituting the name of your desired test for `Testing/testMenu.py`
    *   ```bash
        $ cd src
        $ python -m unittest tests/test_report.py
        ..
        ----------------------------------------------------------------------
        Ran 2 tests in 0.000s

        OK
        ```


## Interpreting Test Results

A progress report is printed as tests are run.  When tests are unsuccessful, more text is printed to help you understand what exactly went wrong.  When many tests fail, you are presented with a lot of confusing text!

The starter code consists of 23 test cases, 2 of which pass.  Of the 21 tests which don't pass, 7 *fail*, which means the tests don't see the expected results.  14 tests result in an *error*, which means that the code under test crashed.  The dispositions of tests are summarized in this table:

Result | Meaning
-------|--------
`ok`   | The test passed
`FAIL` | The code ran, but the expected result was not observed
`ERROR`| The code being tested crashed


### A passing test `ok`

When a test passes you are shown the name of the test method, the full name of the module it belongs to, and its docstring followed by `ok`

```
The year of the Report object can be set from a parameter to the initializer ... ok
test_str (tests.test_report.TestReport.test_str)
```


### A failing test `FAIL`

A test that fails indicates that the code under test ran without crashing but did not yield the expected result.  After all tests have been run, a summary of the failure is printed which displays the line of the test file that failed and an explanation of the problem.

In this example the method `get_emplvl()` returned `None` instead of the expected value `1`:

```
======================================================================
FAIL: test_get_emplvl (tests.test_util.TestUtil.test_get_emplvl)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/fadein/school/Fa23/cs1440/Assn/3-Big_Data/starter/src/tests/test_util.py", line 62, in test_get_emplvl
    self.assertEqual(get_emplvl(self.all_good), 1)
AssertionError: None != 1
```


### A crashing test `ERROR`

The third way a test can conclude is by crashing *unexpectedly* (this means that there is a way to test a function that is *supposed* to crash; read the `unittest` documentation if you are curious).
When the test results in an error the line number of the crash in the unit test is shown, below which you are shown the source code that caused the crash.

In this example the value `"110011"` is searched for in a dictionary called `self.areas`.  However, instead of a dictionary, `self.areas` is the value `None`:

```
======================================================================
ERROR: test_territories (tests.test_area_titles.TestAreaTitles.test_territories)
The areas dictionary contains FIPS codes representing
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/fadein/school/Fa23/cs1440/Assn/3-Big_Data/starter/src/tests/test_area_titles.py", line 116, in test_territories
    self.assertIn("11001", self.areas)  # District of Columbia
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fadein/.pyenv/versions/3.11.5/lib/python3.11/unittest/case.py", line 1137, in assertIn
    if member not in container:
       ^^^^^^^^^^^^^^^^^^^^^^^
TypeError: argument of type 'NoneType' is not iterable
```
