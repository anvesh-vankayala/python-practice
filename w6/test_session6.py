import pytest
import os
import session6
from typing import Callable

## For testing purpose
def add(a:int,b:int):
    """This methods adds two numbers
     Args:
        a: is integer
        b: is integer
     Returns:
        bool value that returns true if func
        __doc__ is more than 50 chars.
       """
    return a+b



def test_session6_readme_exists():
    assert os.path.isfile('README.md'), "README.md is missing"

## Doc string len tester
def test_document_checker_response():
    fu = session6.document_checker()
    assert fu(test_session6_readme_exists) == False, "Something went wrong"
    assert fu(session6.add) == True, "Something went wrong"


def test_document_checker_closure_have_freevar():
    fu = session6.document_checker()
    assert len(fu.__code__.co_freevars) > 0 , "Given function dont have closure"
    assert [cell.cell_contents for cell in fu.__closure__][0] == 50 , "Given free variable value must be 50"

def test_document_checker_is_closure():
    fu = session6.document_checker()
    assert isinstance(fu,Callable) , "document_checker is not closure"
    
def test_document_checker_has_document():
    fu = session6.document_checker()
    assert fu(session6.document_checker) , "Document_checker dont have docs"

