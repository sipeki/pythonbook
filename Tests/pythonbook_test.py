import pytest
from Code import pythonbook


#def test_helloworld():

 #   assert pythonbook.helloworld() == "Hello World"

#def test_helloworld2():

 #   assert pythonbook.helloworld2() == "Hello World"



#def test_parameters():

#    assert pythonbook.parameters() == "Hello World"        # Hello World
#    assert pythonbook.parameters() == ""                   # none
#    assert pythonbook.parameters() == "12334"              # 12334
#    assert pythonbook.parameters() == "$% ^ %"             # $% ^ %
#    assert pythonbook.parameters() == "  $% ^ %"           # <space><sapac>$% ^ %

#def test_parametersoperators():

#    assert pythonbook.parametersoperators() == 1           # 1 0
#    assert pythonbook.parametersoperators() == 0           # 0 0
#    assert pythonbook.parametersoperators() == 2           # 1 1
#    assert pythonbook.parametersoperators() == -2          # -1 -1
#    assert pythonbook.parametersoperators() == 0            # 1 -1
#    assert pythonbook.parametersoperators() == 24           # 12 12

#def test_conditionals():
#    assert pythonbook.conditionals() == 1  # 1 0 true
#    assert pythonbook.conditionals() == 1  # 1 0 false
#    assert pythonbook.conditionals() == 0  # 0 0 true
#    assert pythonbook.conditionals() == 0  # 0 0 false
#    assert pythonbook.conditionals() == -2  # -1 -1 true
#    assert pythonbook.conditionals() == 0  # -1 -1 false
#    assert pythonbook.conditionals() == 14  # 12 2 true
#    assert pythonbook.conditionals() == 10  # 12 2 false


#def test_conditionals2():
#    assert pythonbook.conditionals2() == 1  # 1 0
#    assert pythonbook.conditionals2() == 1  # 0 1
#    assert pythonbook.conditionals2() == 14  # 12 2


def test_recursion():

    assert pythonbook.recursion() == "1 1 1 1 1 1 1 1 1 1"
    assert pythonbook.recursion() == "2 3 5 7 9 11 15 19 21 22"     # 1 1 2 1 2 3 4 3 4 5 6 5 7 8 9 10 11 10 12 10
