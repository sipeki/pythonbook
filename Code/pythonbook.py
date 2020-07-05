
#def helloworld():

 #   return "Hello World"


#def helloworld2():


#    text = "Hello World"
#    return text

#def parameters():

#    val = input("Please input something nice")

#    return val

# def parametersoperators():

#    return int(input("Please input number: ")) + int(input("Please input number: "))

def conditionals():

    par1 = int(input("Please input a number: "))
    par2 = int(input("Please input a number: "))
    par3 =  input("True or False ")

    if par3.lower() == "true":
        summed = par1 + par2
    else:
        summed = par1 - par2



    return summed


def conditionals2():

    par1 = int(input("Please input a number: "))
    par2 = int(input("Please input a number: "))

    if par1 == 0:
        value = par2
    elif par2 == 0:
        value = par1
    else:
        value = par1 + par2

    return value


def recursion():

    result = ""     # set variable value to empty

    for i in range(10):     # loop ten times

        if result == "":
            result = str(conditionals2())    # append the result to variable to the next result
        else:
            result = result + ' ' + str(conditionals2())

    return result

# Lists
# Create a list with 10 integer values in it, then call and output the first element in the list.

def pllists():

    thelist = []

    for i in range(10):     # loop ten times
        thelist.append(i+1)

    result = thelist[0]

    return result

#Recursion/Lists
# Using your list that you created in the Lists task, create a loop that iterates through your list,
# outputting the values contained within it.

def pllists2():

    thelist = []

    for i in range(10):     # loop ten times
        thelist.append(i+1)

    return thelist

def recursionlists():

    thelist = pllists2()
    newlist = []
    for i in range(len(thelist)):

        newlist.append(thelist[i])

    return newlist

#   Create a loop that populates a list with values, outputting them at each iteration.
#   Then create another loop that iterates through the array, changing the values at each
#   point to equal itself times 10, outputting them at each iteration.
#   Example Output
#   1,2,3,4…
#   10,20,30,40…


def recursionlists2():

    thelist = []
    secondlist = []

    for i in range(10):     # loop ten times
        thelist.append(i+1)

    for i in range(len(thelist)):

        secondlist.append(thelist[i]*10)

    return thelist, secondlist

#   User input
#   Modify the previous task to take input from the user, taking
#   an integer off of the user and using that integer to determine how large the array is going to be.

def userinput():

    thelist = []
    secondlist = []
    rangevalue = int(input("Please enter a value? "))

    if rangevalue > 0:                  # if value greater than 0
        for i in range(rangevalue):     # loop to the value of the range
            thelist.append(i+1)
    else:
        # startrange = rangevalue * -1
        for i in range(0,rangevalue,-1):     # loop to the value of the range
            thelist.append(i-1)

    for i in range(len(thelist)):
        secondlist.append(thelist[i]*10)

    return thelist, secondlist

#   Functions
# Create a function that asks the user for a number and whether they want to double or triple the number.
# Have methods within the function for doubling and tripling the user’s number.


def plfuctions():

    val = int(input("\n Enter a number, any number: "))

    while True:
        data = input("If you wish to double " + str(val) + " press d or to triple the " + str(val) + " press t? ")
        if data.lower() not in ('d', 't'):
            print("Please respond with either a 'd' or 't'. Let's see if you can get it right this time.")
        else:
            break

    if data.lower() == "d":
        answer = int(val)*2
    else:
        answer = int(val) * 3

    return answer

#   Easy Exercise – Grade Calculator
#   Challenge
#   Create an application which asks the user for an input for a maths mark, a chemistry mark and a physics mark.
#   Add the marks together, then work out the overall percentage. And print it out to the screen.
#   If the percentage is below 40%, print “You failed”
#   If the percentage is 40% or higher, print “D”
#   If the percentage is 50% or higher, print “C”
#   If the percentage is 60% or higher, print “B”
#   If the percentage is 70% or higher, print “A”


def gradercalc():

    mathsmark = int(input("Please enter your maths mark: "))
    chemmark = int(input("Please enter your chemistry mark: "))
    physicsmark = int(input("Please enter your physics mark: "))
    mark = (mathsmark + chemmark + physicsmark)/3  # assumed each exam was worth 100

    if mark >= 70:
        grade = "A"
    elif mark <= 69 and mark >= 60:
        grade = "B"
    elif mark <= 59 and mark >= 50:
        grade = "C"
    elif mark <= 49 and mark >= 40:
        grade = "D"
    elif mark < 40:
        grade = "Fail"

    return grade

#   ISBN's (International Standard Book Numbers) are identifiers for books.
#
# The ISBN is a thirteen-digit code.
#
# The last digit is a check number calculated as follows:
# The first 12 digits are taken
# Starting at index 1, if the index is odd - add it, and if the index is even – multiply the digit by three then add it.
# From the sum find the remainder after dividing by 10.
# 10 minus the remainder give us the check digit
# In other words the following algebra would give us the check digit:
# ( 10 – (( x1 + 3x2 + x3 + 3x4 + x5 + 3x6 + x7 + 3x8 + x9 + 3x10 + x11 + 3x12 ) % 10))
#
# For ISBN: 978-0-306-40615-? The following check would happen:
# 9 +  3*7 +   8 +   3*0 +   3 +   3*0 +   6 +  3*4 +   0 +  3*6 + 1 +  3*5 = 93
# 93 / 10 =


def isbncheck(input):
    # isbn example 978-0-306-40615
    isbn = input.replace("-", "")
    chksum = 0

    for i in range(0,11,2):
        chksum = int(isbn[i]) + chksum
        chksum = (int(isbn[i+1])*3) + chksum

    r1 = chksum % 10
    chksum = 10 - r1

    return chksum

#   Create a function that when given two strings of letters,
#   determine whether the second can be made from the
#   first by removing one letter. The remaining letters must
#   stay in the same order.
# Example
# near ("reset", "rest") => true
# near ("dragoon", "dragon") => true
# near ("eave", "leave") => false
# near ("sleet", "lets") => false
# https://www.askpython.com/python/string/remove-character-from-string-python

def near(txt1, txt2):

    #for i in range(len(txt1)):
     #   txtchk = txt1.replace(txt1[i],'',1)

    for i in range(len(txt1)):
        txtchk = txt1[:i - 1] + txt1[i:]    # slice from start set by i minus 1
        if txtchk == txt2:
            break



    return txtchk == txt2




