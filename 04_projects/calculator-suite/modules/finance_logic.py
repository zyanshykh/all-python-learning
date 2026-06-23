def calculate_emi(principal, tenure_years, interest_rate):
    r = (interest_rate / 12) / 100
    n = tenure_years * 12
    emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return emi, emi * n, (emi * n) - principal