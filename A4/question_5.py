import doctest


TOLERANCE = 0.01


def cash_money(cash: float) -> dict:
    """
    Return a dictionary equal to the parameter cash split up into it's keys.

    :param cash: Float.
    :precondition: Must be a positive float.
    :postcondition: Determine how many bills/coins (keys) are need to equate to the given cash value.
    :return: A dictionary which equal to the cash value split up into various bills/coins

    >>> cash_money(188.41)
    {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 1}
    >>> cash_money(50.00)
    {100: 0, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    >>> cash_money(0.01)
    {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 1}
    """
    if cash < 0:
        raise ValueError('Must be a positive double over 0!')
    cash_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    for bill_coin_amount, amount_of_cash in cash_dict.items():
        if bill_coin_amount < cash or abs(bill_coin_amount - cash) < TOLERANCE:
            amount_of_cash = round(cash, 2) // bill_coin_amount
            cash_dict[bill_coin_amount] += int(amount_of_cash)
            cash -= bill_coin_amount * amount_of_cash
    return cash_dict


def main():
    print(cash_money(188.41))


if __name__ == "__main__":
    main()
    doctest.testmod()
