"""
Module: Functions and Scopes
Topic: Reusability, Dynamic Arguments (*args, **kwargs), and Scope resolution.
"""

# 1. Function with type hinting and docstrings (Best Practice)
def calculate_invoice(subtotal: float, tax_rate: float = 0.15) -> float:
    """
    Calculates the total price including tax.
    """
    return subtotal + (subtotal * tax_rate)


# 2. Dynamic Arguments (*args for tuples, **kwargs for dictionaries)
def build_user_profile(username: str, *skills, **additional_info) -> dict:
    """
    Creates a dynamic user profile for startup team onboarding.
    """
    profile = {
        "username": username,
        "skills": list(skills),
        "metadata": additional_info
    }
    return profile


# 3. Scope Demonstration (Global vs Local)
counter = 100 # Global variable

def increment_counter():
    global counter # Modifying global state (use carefully in production)
    counter += 1
    local_val = "I am local"
    print(f"[Local Scope] Inside function: {local_val}")


# --- Execution ---
if __name__ == "__main__":
    print("--- 1. Functions & Dynamic Args ---")
    total = calculate_invoice(5000) # Uses default tax 15%
    print(f"Total Invoice: PKR {total}")
    
    user = build_user_profile("Frank", "Python", "Next.js", "TypeScript", role="Founder", status="Active")
    print(f"User Profile: {user}\n")
    
    print("--- 2. Scope Resolution ---")
    increment_counter()
    print(f"[Global Scope] Global counter value now: {counter}")