# Assignment 5: Grades

> [!IMPORTANT]
> This assignment is to be completed individually. It is not a team project.  You must document (using comments in your code) all resources (beyond our official textbook, Canvas, the class discussion forum, or the class website) that you used to help you complete this assignment. For example, if you referenced a code example from an online website such as Stackoverflow or github you could acknowledge it as follows: 
>
> ```
> # Next we print 'Hello, World' to the console.
> # Based on help from: https://stackoverflow.com/questions/826948/syntax-error-on-print-with-python-3
> print("Hello, world!")
> ```
>
> You must provide an attribution to any resource you consulted to complete this assignment except for our official textbook, Canvas, the class discussion forum, or the class website. Resources that require attribution include — but are not limited to — AI tools (even those built in to VS Code), websites, books, notes from other students, tutors, or help from other people (friends, classmates, etc.). Under no circumstances are you to look at or copy any material related to another person's solution for this assignment.
>
> To repeat, you must attribute any resource you consulted to complete this assignment other than our official textbook, Canvas, class discussion forum, or the class website. You must cite all AI technologies you used, if any, to complete this assignment. Failure to provide attribution is a violation of the honor code.

## Overview

For this assignment, you'll be reading grade data from a file, determining student letter grades, and writing the results to a new file. The details for how your program should work are described in the Basic Requirements and Advanced Requirements sections below.

**Input Data.** A sample input data file of the type that your program should process is available in the repository file named *sample_input.txt*. The sample file contains fake grade data for 14 students. However, your program should be able to work with a file with an arbitrary number of students. For example, I may test your program with just 3 students, or with 300. Your program should work for any length file. It should also be able to detect and gracefully accomodate errors in the input file as described in the requirements sections below.

Each student record spans 3 lines in the input data file. The first line contains the type of student: GRAD or UNDERGRAD. This is important because graduate and undergraduate students get graded differently at UNC. The second line contains the student's name. The third line contains the student's overall numerical grade. Your program will need to map these to letter grades according to the following rules:

For the sake of this assignment, GRAD student grades are defined as follows:

| Number Range | Letter Grade |
| ------------ | ------------ |
| 95-100       | H            |
| 80-94        | P            |
| 70-79        | L            |
| 0-69         | F            |

For the sake of this assignment, UNDERGRAD student grades are defined as follows:

| Number Range | Letter Grade |
| ------------ | ------------ |
| 90-100       | A            |
| 80-89        | B            |
| 70-79        | C            |
| 60-69        | D            |
| 0-59         | F            |

Please note that grades for this course are assigned as outlined in the course syllabus. The grading scales specified above are for use only in the context of this assignment.

**Output Data.** Your program should write the results of its computations to an output file. An example of the required output file can be found in the repository file named *sample_output.txt*. The sample file contains fake grade data for 14 students. Each student record spans 2 lines in the data file. The first line for a student contains the student name. The second line for a student contains the student's letter grade.

## Basic Requirements

> [!NOTE]
> Satisfying only the basic requirements perfectly, with no points deducted for any reason, would earn a maximum score of 8 out of 10 for this assignment.

Your program should perform the following:

* Prompt the user to enter the name of the input file, making sure that the file exists and asking the user to re-enter a filename if needed.
* Prompt the user to enter the name of an output file. The output file should be erased/overwritten if an old one with the same name exists.
* Read the input file, assign grades as appropriate for the type of student (GRAD vs. UNDERGRAD), and write the output to file.
* Gracefully handle errors in the input file. In particular, your program should catch errors such as invalid numbers for grades, or student categories that are not "GRAD" or "UNDERGRAD". If found, the program should display an error message telling the user what the problem was. The program should then stop processing the rest of the data file and tell the user to fix the problems before retrying. During grading, your program will be tested with input files that have had errors intentionally introduced. It is suggested that you try this in your own testing to make sure that your program works as expected.

Two kinds of output should be produced by your program. First, an output data
file should be created using the same format described in the "Output Data"
paragraph of the Overview section above. Second, your program will produce
output on the console in the form of status messages and prompts for user
input. The console output produced by your program should be nearly identical to the
sample output provided below. 
While the specific data (names, grades, etc.) will vary based on the input provided, the data formats, prompts, and messages
printed to the console when using your program should match those in the sample
output files to receive full credit.



## Advanced Requirements

> [!NOTE]
> Satisfying both the basic and advanced requirements perfectly, with no points deducted for any reason, will result in a full 10 out of 10 score for this assignment.

Expand on the basic requirements by extending your program as follows.

* Allow the user if they wish to subject the grades to a curve prior to grading.
* If the user declines to curve the grades, the program should proceed as outlined in the Basic Requirements.
* If the user chooses to curve the grades, the program should ask the user to enter the number grade that should be treated as a "100" for grading purposes.
* Once the should enters a number, the program should use this to curve the grades using linear interpolation. For example:
    * If a user enters "50" as the score to use for the curve, then the following "curved grades" should be used when assigning letters:
        * 25 becomes 50
        * 50 becomes 100
        * 100 becomes 200
    * If a user enters "80" as the score to use for the curve, then the following "curved grades" should be used when assigning letters:
        * 40 becomes 50
        * 80 becomes 100
        * 100 becomes 125
* Pay attention to possible exceptions. Make sure that your code for this feature is robust.

## Sample Console Output

The program should produce output data files as described in the Overview section of this assignment description.  In addition, the program should also produce output on the console as shown here.  

More specifically, this example console output shows what the output should look like when the user processes grades without a curve and no errors are detected:

```
Please enter the name of the input data file: grade_input.txt
Please enter the name of the output data file: grade_output.txt
Would you like to curve the grades? (Y/N) N
All data was successfully processed and saved to the requested output file.
```

When the user decides to apply a curve, the console output should look like this:
```
Please enter the name of the input data file: grade_input.txt
Please enter the name of the output data file: grade_output.txt
Would you like to curve the grades? (Y/N) Y
Please enter the score that should map to a '100%' grade: 75
All data was successfully processed and saved to the requested output file.
```

Finally, here is an example of what the console output should look like when an error is detected:
```
Please enter the name of the input data file: grade_input_with_bad_student_type.txt
Please enter the name of the output data file: grade_output.txt
Would you like to curve the grades? (Y/N) N
Unknown student category detected (HIGHSCHOOL).
Error occurred while determining letter grade. Aborting.
```

For an example of the expected output data file, see this repository's sample_output.txt file.

## Grading Criteria

This assignment will be graded on a 10 point scale. Your grade for this assignment will be based on a combination of factors, including:

* Correct functionality (e.g., Does your Python code do what it is supposed to do as outlined in the basic and/or advanced requirements?)
* Clarity of your solution (e.g., Did you solve the problem directly and efficiently? Or is your answer excessively complex and/or inefficient?)
* Coding style (e.g., Is your code readable with comments, meaningful variable names, and good whitespace/indentation?)
* Meets submission requirements (see below)

## Seeking Help

For general questions about Python, please use the class forum on Piazza to seek assistance. For questions that are personal in nature or that would reveal a solution to the assignment, you ask for help by email or during office hours. However, please note that emailed questions will not receive an immediate response. It is likely that it will take 24-48 hours for me to respond.

## Submitting Your Solution

When you have completed your work on the assignment, it is time to submit your solution via Canvas.  You can submit your assignment by taking the following steps:
1. Be sure that all of your changes have been pushed to your GitHub repository for the assignment.
2. Go to the web page for your repository on github.com
3. Click the green button labeled "< > Code &#9660;" which should open a popup menu.
4. From the popup menu, click on "Download ZIP" which will download a zip file containing your entire project to your computer. 
5. Submit the zip file you just downloaded via Canvas as your solution for this assignment.


> [!WARNING]
> NOTE FOR MAC USERS: Mac users who use the Safari browser will notice that the browser will, by default, automatically unzip and delete zip files you download from the internet. To change this behavior, press and hold the Option key when clicking the "Download ZIP" menu item.  This will prevent Safari from automatically unzipping and deleting the Zip file. Instead, it will just download the Zip file as it is just as you would get on any other browser.  Only Safari users need to take this extra step.


## Due Date

The due date for this assignment can be found in the official class schedule and on Canvas.

