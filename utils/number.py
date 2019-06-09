from decimal import Decimal

def indian_formatted_currency(amount):
    prefix = ""
    if amount<0:
        prefix = "-"
    amount = abs(int(round(amount)))
    amount, thousands = divmod(amount, 1000)
    if amount > 0:
        thousands = str(int(thousands)).zfill(3)
    groups = [thousands]
    while amount:
        amount, group = divmod(amount, 100)
        if amount > 0:
            group = str(group).zfill(2)
        groups.insert(0, group)
    result = ','.join(map(str, groups))
    return prefix + result