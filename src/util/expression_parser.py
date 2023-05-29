from sympy import simplify, symbols

def string_to_expression(string_expression: str):
    """
    Convert a string representation of a mathematical expression to a SymPy expression and simplify it.

    - Parameters:
        - string_expression (str): The string representation of the mathematical expression.

    - Returns:
        - expression (SymPy expression): The simplified SymPy expression.
    """
    return simplify(string_expression)    
    
X, Y, Z = symbols('x y z')
PARAMETER = symbols('t')

def evaluate_parametric_expression(expression, parameter):
    """
    Evaluate a parametric expression by substituting a value for the parameter.

    - Parameters:
        - expression (SymPy expression): The parametric expression.
        - parameter (float): The value to substitute for the parameter.

    - Returns:
        - result (float): The numerical result of evaluating the parametric expression.
    """
    return float(expression.subs(PARAMETER, parameter))

def evaluate_string_numerical_expression(string_expression: str):
    """
    Evaluate a string representation of a numerical expression and return the numerical result.

    - Parameters:
        - string_expression (str): The string representation of the numerical expression.

    - Returns:
        - result (float): The numerical result of evaluating the expression.
    """
    return string_to_expression(string_expression).evalf()