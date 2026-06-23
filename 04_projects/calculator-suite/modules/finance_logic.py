def calculate_emi(principal, tenure_years, interest_rate):
    """
    Calculates monthly EMI based on reducing balance method.
    Returns: (emi, total_payment, total_interest)
    """
    r = (interest_rate / 12) / 100
    n = tenure_years * 12
    emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return emi, emi * n, (emi * n) - principal

def calculate_ci(p, rate, time):
    future_value = p * ((1 + (rate / 100)) ** time)
    net_interest = future_value - p
    return future_value, net_interest