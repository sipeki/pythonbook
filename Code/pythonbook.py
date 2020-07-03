
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


