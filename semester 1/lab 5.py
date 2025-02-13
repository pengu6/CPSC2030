"""
Complete the following functions based on the description in their docstring.

When functions are underspecified, implement them so that the tests pass.
"""

def square(n):
    """
    Return the square of input `n`

    :param n: The number to square
    :return: The square of `n`
    """
    
    return n*n


assert(square(0) == 0)
assert(square(1) == 1)
assert(square(2) == 4)
assert(square(25) == 625)


def letter_grade(percentage):
    """
    Return a letter grade from a supplied percentage
    
    :param percentage: Grade a percentage
    :return: Letter grade as a string (e.g. "B+")
    
    This function uses the following grading scale:

    Letter Grade   Percentage
    ------------   ----------
    A              93-100%
    A-             90-93%
    B+             87-90%
    B              83-87%
    B-             80-83%
    C+             77-80%
    C              73-77%
    C-             70-73%
    D+             67-70%
    D              63-67%
    D-             60-63%
    F              0-60%
    ------------   --------
    """
    if percentage >= 100:
        return("A")
    elif percentage >= 90:
        return("A-")
    elif percentage >= 87:
        return("B+")
    elif percentage >= 83:
        return("B")
    elif percentage >= 80:
        return("B-")
    elif percentage >= 77:
        return("C+")
    elif percentage >= 73:
        return("C")
    elif percentage >= 70:
        return("C-")
    elif percentage >= 67:
        return("D+")
    elif percentage >= 63:
        return("D")
    elif percentage >= 60:
        return("D-")
    elif percentage <= 60:
        return("F")

assert(letter_grade(100) == "A")
assert(letter_grade(90) == "A-")
assert(letter_grade(87) == "B+")
assert(letter_grade(83) == "B")
assert(letter_grade(80) == "B-")
assert(letter_grade(77) == "C+")
assert(letter_grade(73) == "C")
assert(letter_grade(70) == "C-")
assert(letter_grade(67) == "D+")
assert(letter_grade(63) == "D")
assert(letter_grade(60) == "D-")
assert(letter_grade(59) == "F")
assert(letter_grade(84.5) == "B")
assert(letter_grade(79.9) == "C+")


def get_age(birth_year, birth_month, birth_day,
            current_year, current_month, current_day):
    """ Returns an person's age given their birthdate

    :param birth_year: Birth year as an integer
    :param birth_month: Birth month as an integer
    :param birth_day: Birth day as an integer
    :param current_year: Current year as an integer
    :param current_month: Current month as an integer
    :param current_day: Current day as an integer
    """
    #get_age = current_year - birth_year
    getdays = current_year * 365
    getbirth = birth_year * 365
    getdays1 = current_month * 30
    getbirth2 = birth_month * 30
    currentdate = getdays + getdays1 + current_day
    birthdate = getbirth + getbirth2 + birth_day
    getage = currentdate - birthdate
    get_age = getage // 365
    return(get_age)
    


assert(get_age(1906,1,1,2006,1,1) == 100) #Jan 1st 1906, day jan 1st 2006
assert(get_age(2030,1,1,2030,1,1) == 0)#Jan 1st 2030, day jan 1st 2030
assert(get_age(2030,1,1,2031,1,1) == 1)#Jan 1st 2030, day jan 1st 2031
assert(get_age(2030,6,1,2031,1,1) == 0)#Jan 6th 2030, day jan 1st 2031
assert(get_age(2030,6,6,2036,6,6) == 6)#june 6th 2030, day June 6th 2036
assert(get_age(2030,6,6,2036,6,5) == 5)#june 6th 2030, day June 5th 2036
assert(get_age(2030,6,6,2036,5,6) == 5)#June 6th 2030, day May 6th 2036
assert(get_age(2030,4,6,2036,5,6) == 6)#April 6th 2030, day May 6th 2036


# TODO: Create a custom function below of your choosing.

import math

def square_root(w):
    if w == 25 or 36 or 49 or 64 or 81 or 100:
        return math.sqrt(w)
    elif w <=10:
        return("Not a perfect square")


assert(square_root(25) == 5)
assert(square_root(36) == 6)
assert(square_root(49) == 7)
assert(square_root(64) == 8)
assert(square_root(81) == 9)
assert(square_root(100) == 10)
# The function should do something meaningful and use branches **and** arithmetic.
#
# Include meaningful tests using `assert`.