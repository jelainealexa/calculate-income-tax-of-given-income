# Calculate income tax for the given income by adhering to the rules below

# Given
tax_income = 50000
tax_payable = 0

def calculate_income_tax(taxable_income):
    # If taxable income is less than or equal to $10,000
    if taxable_income <= 10000:
        tax_payable = taxable_income * 0

    # If taxable income is between $10,001 and $20,000
    elif taxable_income <= 20000:
        tax_payable = (taxable_income - 10000) * 0.10
        
    # If taxable income is above $20,000
    else:
        tax_payable = 10000 * 0.10 + (taxable_income - 20000) * 0.20

    return tax_payable

tax_payable = calculate_income_tax(tax_income)

# Print result
print(f"With the given income of", tax_income)
print(f"Tax payable is", tax_payable)