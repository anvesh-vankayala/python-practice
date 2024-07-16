import pytest
import os
import session6
from typing import Callable
from session6 import function_tracker

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

## Q1 : Doc string len tester
def test_document_checker_response():
    fu = session6.document_checker()
    assert fu(test_session6_readme_exists) == False, "Something went wrong"
    assert fu(session6.add) == True, "Something went wrong"


def test_document_checker_closure_have_freevar():
    fu = session6.document_checker()
    assert len(fu.__code__.co_freevars) > 0 , "Given function dont have freevars"
    assert [cell.cell_contents for cell in fu.__closure__][0] == 50 , "Given free variable value must be 50"

def test_document_checker_is_closure():
    fu = session6.document_checker()
    assert isinstance(fu,Callable) , "document_checker is not closure"
    
def test_document_checker_has_document():
    fu = session6.document_checker()
    assert fu(session6.document_checker) , "Document_checker dont have docs"

## Q2 : Fibonacci tester

def test_fibonacci_closure_have_freevar():
    fu = session6.fibonacci_numbers()
    assert len(fu.__code__.co_freevars) > 0 , "Given function dont have freevars"

def test_fibonacci_closure_is_right():
    fu = session6.fibonacci_numbers()
    assert [fu() for i in range(0,10)] == [1,2,3,5,8,13,21,34,55,89] , "Some thing went wrong"

# test_fibonacci_closure_is_right()

## Q3: function tracker tester
def test_function_tracker_test_add():
    @function_tracker
    def add(a,b):
        return a+b
    add(3,4)
    assert session6.func_count_tracker['add'] == 1, "Global varibale is not updated,some hting went wrong"

def test_function_tracker_test_mul():
    @function_tracker
    def mul(a,b):
        return a*b
    mul(3,4)
    mul(3,4)
    assert session6.func_count_tracker['mul'] == 2, "Global varibale is not updated,some hting went wrong"

def test_function_tracker_test_div():
    @function_tracker
    def div(a,b):
        return a+b
    div(3,4)
    assert session6.func_count_tracker['div'] == 1, "Global varibale is not updated,some hting went wrong"


def test_function_tracker_is_closure():
    fu = session6.function_tracker(lambda a,b : a+b)
    assert isinstance(fu,Callable) , "document_checker is not closure"

def test_function_tracker_has_document():
    fu = session6.document_checker()
    assert fu(session6.function_tracker) , "Document_checker dont have docs"

def test_function_tracker_full_test():
    print(session6.func_count_tracker)
    assert session6.func_count_tracker == {'add': 1, 'mul': 2, 'div': 1}, "Global varibale is not updated,some hting went wrong"