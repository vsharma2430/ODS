import math

gravity_constant = 9.80665

def roundOff(value : float) : 
    return str('{:,.2f}'.format(round(value,3)))

def pass_fail(check:bool):
    return "(PASS)" if check == True else "(FAIL)"

def tonneToN (value:float):
    return value * 1000 * gravity_constant