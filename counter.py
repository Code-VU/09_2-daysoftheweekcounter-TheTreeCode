def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    fhand = open(file_name)
    daysoftheweek = dict()
    for line in fhand:
        if line.startswith('From '):
            currentlineaslist = line.split()
            daysoftheweek[currentlineaslist[2]] = daysoftheweek.get(currentlineaslist[2], 0) + 1
    print(daysoftheweek)


## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()



'''
Assignment
Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print out the contents of your
dictionary (order does not matter).

Sample Line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Starter Code
file_name = input("Enter a file name: ")
Desired Output
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
Hint
The desired output needs to be printed as described in the assignment, if it is not, the tests will
fail.
'''