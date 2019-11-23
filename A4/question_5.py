def cash_money(cash: float) -> dict:
    cash_dict = {50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    for k, v in cash_dict.items():

        cash_dict[k] += 1
    return cash_dict


print(cash_money(55.05))