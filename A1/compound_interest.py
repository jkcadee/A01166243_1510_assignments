def compound_interest(principal, annual_interest, interest_compound_yearly, account_growth):
    """Takes four parameters and plugs them into a function of arithmetic operators"""
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
    print(compound_interest(6.3, 0.1, 2, 9))
    return


if __name__ == "__main__":
    main()