import pytest
from Code import pythonbook


#def test_helloworld():

 #   assert pythonbook.helloworld() == "Hello World"

#def test_helloworld2():

 #   assert pythonbook.helloworld2() == "Hello World"



def test_parameters():

    assert pythonbook.parameters() == "Hello World"        # Hello World
    assert pythonbook.parameters() == ""                   # none
    assert pythonbook.parameters() == "12334"              # 12334
    assert pythonbook.parameters() == "$% ^ %"             # $% ^ %
    assert pythonbook.parameters() == "  $% ^ %"           # <space><sapac>$% ^ %
