TOLERANCE = 0.01


def cash_money(cash: float) -> dict:
    cash_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    for bill_coin_amount, amount_of_cash in cash_dict.items():
        if bill_coin_amount < cash or abs(bill_coin_amount - cash) < TOLERANCE:
            amount_of_cash = round(cash, 2) // bill_coin_amount
            cash_dict[bill_coin_amount] += int(amount_of_cash)
            cash -= bill_coin_amount * amount_of_cash
    return cash_dict


def main():
    print(cash_money(55.15))


if __name__ == "__main__":
    main()