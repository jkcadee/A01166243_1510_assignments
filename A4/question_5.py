def cash_money(cash: float) -> dict:
    cash_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    for k, v in cash_dict.items():
        if k < cash:
            amount_of_cash = cash // k
            cash_dict[k] += int(amount_of_cash)
            print(cash)
            cash = round(cash - (k * amount_of_cash), 2)
            print(cash)
    return cash_dict


print(cash_money(55.15))
