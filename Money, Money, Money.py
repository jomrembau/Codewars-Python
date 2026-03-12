def calculate_years(principal, interest, tax, desired):
    num_years = 0
    while principal < desired:
        interest_amount = principal * interest
        after_tax= interest_amount * tax
        year_interest = interest_amount - after_tax
        principal = principal + year_interest
        num_years = num_years + 1
    return  num_years

print(calculate_years(1000, 0.05, 0.18, 1100))