import doctest


def compound_interest(principal, annual_interest, interest_compound_yearly, account_growth):
    """Takes four parameters and plugs them into a function of arithmetic operators
    >>> compound_interest(3, 0.2, 1, 5)
    7.464959999999998
    >>> compound_interest(2, 0.1, 6, 4)
    2.9738292358927154
    """
    result = principal * (1 + annual_interest / interest_compound_yearly) ** (interest_compound_yearly * account_growth)
    return float(result)


"""
Return the result of the operation as a float.

:param principal: float
:param annual_interest: float
:param interest_compound_yearly: int
:param account_growth: int
:precondition: principal must be a float
:precondition: annual_interest must be a float
:precondition: interest_compound_yearly must be an int
:precondition: principal must be an int
:postcondition: Add 1 plus annual_interest divided by interest_compound_yearly to the power of interest_compound_yearly
                multiplied by account_growth. Multiply by principal.
:return: A float as the result from the operation.
"""


def main():
    """Executes the program"""
    print(round(compound_interest(6.3, 0.1, 2, 9), 2))
    return


if __name__ == "__main__":
    main()
    doctest.testmod()
"""
I used automation mainly to create this function, as you are just inputting for arguments into the function. The
function is mainly made of arithmetic operators. Since the equation is so simple, it could be said that abstraction was
used as well.
"""