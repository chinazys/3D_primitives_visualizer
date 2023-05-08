from sympy import simplify, symbols

def string_to_expression(string_expression: str):
    return simplify(string_expression)    
    
X, Y, Z = symbols('x y z')
PARAMETER = symbols('t')

def evaluate_parametric_expression(expression, parameter):
    return float(expression.subs(PARAMETER, parameter))

