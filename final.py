"""
The program is looking to create a function that will calculate the perecent of grades
that are above that average score
The program is going to open file "final(1).txt"
It will then calculate the percentage of grades that are above average
it will gather all the grades from the file "final(1).txt"
it will add all grades and then calculate the average grade score
it will return the count and multiply the count by 100 then divide by the count of grades

The program will define a main function to kick start the next series 
it wil open the file and set grades to a empty list which will be imported from the file "final(1).txt"
it will append the grades and then print the number of grades
next the average is set to 0 so that it can be calculated
the average score is then divided by the count of grades to check how many grades are above average
the percent of grades that are above average is then calculated
print to the user the average grade score
print to the user the percent of grades that are above average
close the file 

"""

"""
define calculate percent above average 
set count equals 0
use if statement to explain grade is greater than average score
add the number of count +1 to get average 
then return the count and * by 100 and divide by number of grades in total

define main
open file "final(1).txt"
set grades to an empty list
use for statement to automate the list of grades
append the grades and strip
print the grade count to user
set average to 0
use for statement to get the grade in grades
add average with grade
print average grade 
print percentage of grades above average (calculate the percen of grades that are above average)
close file
call main function 
"""


def calculate_percent_above_average(grades, average):
    count = 0
    for grade in grades:
        if grade > average:
            count += 1
    return (count * 100) / len(grades)

def main():
    file = open('Final.txt')
    grades = []
    for line in file:
        grades.append(int(line.strip()))
    print("Number of grades: ", len(grades))
    average = 0
    for grade in grades:
        average += grade
    average /= len(grades)
    print("Average grade: ", average)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades, average)))
    file.close

main()