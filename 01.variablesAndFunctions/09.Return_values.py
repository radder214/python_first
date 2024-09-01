def tax_calc(money = 0): # 0 = default parameter
    return money * 0.35
taxVal = tax_calc(1000000)

def pay_tax(tax = 0): # 0 = default parameter
    print(f"need to pay {tax}")
pay_tax(taxVal)
pay_tax(tax_calc(2000000))
pay_tax()