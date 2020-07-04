
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


print(recursionlists2())

