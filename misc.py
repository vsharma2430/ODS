import math

gravity_constant = 9.80665

def roundOff(value : float) : 
    return str('{:,.2f}'.format(round(value,3)))

value_delta = 0.0001
def compare_value_delta(value1:float,value2:float,delta:float):
    if(abs(value1-value2)<abs(delta)):
        return True
    else:
        return False

def pass_fail(check:bool):
    return "(PASS)" if check == True else "(FAIL)"

def tonneToN (value:float):
    return value * 1000 * gravity_constant

def MPaToPa(value:float):   #oe N/mm2 to Pa
    return value*1000000

def PaToMPa(value:float):
    return value/1000000

def quadratic_solver(a:float,b:float,c:float):
    x1:float = 0
    x2:float = 0
    d=b*b-4*a*c

    if(compare_value_delta(d,0,value_delta)):
        x1= -b/(2*a)
        return [x1]
    elif(d>0):
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        return [x1,x2]
    else:
        return []