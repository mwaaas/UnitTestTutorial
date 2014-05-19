'''
Created on Jan 3, 2014

@author: mwas
'''
class NonIntegerError(Exception):pass

def find_even(number):

    if type(number) is not int:
        raise NonIntegerError
    return number % 2 == 2
